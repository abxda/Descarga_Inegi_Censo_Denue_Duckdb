import os
import glob
import duckdb
import geopandas as gpd
from . import config

def build_database():
    """Crea y puebla la base de datos DuckDB con los datos procesados."""
    print("--- Iniciando Construcción de la Base de Datos DuckDB ---")

    if os.path.exists(config.DB_PATH):
        os.remove(config.DB_PATH)
        print(f"INFO: Base de datos anterior eliminada en {config.DB_PATH}")

    con = duckdb.connect(config.DB_PATH)
    con.execute("INSTALL spatial; LOAD spatial;")

    # Limitar la memoria a 10GB para evitar errores en sistemas con poca RAM
    con.execute("PRAGMA memory_limit='10GB'")

    # --- 1. Procesar y Cargar DENUE ---
    print("\nPaso 1/3: Creando tabla 'denue'...")
    denue_geoparquet_files = glob.glob(os.path.join(config.DENUE_GEOPARQUET_DIR, '*.geoparquet'))
    if denue_geoparquet_files:
        # Estrategia de carga robusta para geometrías:
        # 1. Cargar GeoParquet en un GeoDataFrame de GeoPandas.
        # 2. Convertir la columna de geometría a texto WKT (Well-Known Text).
        # 3. Cargar el DataFrame (sin la geometría original) en una tabla temporal de DuckDB.
        # 4. Crear la tabla final usando ST_GeomFromText para que DuckDB reconstruya la geometría
        #    a partir del WKT. Esto evita problemas de interpretación del formato binario WKB
        #    entre la escritura de GeoPandas y la lectura de DuckDB.
        gdf_denue = gpd.read_parquet(denue_geoparquet_files)
        gdf_denue['geometry_wkt'] = gdf_denue.geometry.to_wkt()
        df_denue = gdf_denue.drop(columns=['geometry'])
        
        con.execute("CREATE TEMP TABLE temp_denue_wkt AS SELECT * FROM df_denue")
        sql_create_denue = """
            CREATE TABLE denue AS 
            SELECT *, ST_GeomFromText(geometry_wkt) AS geometry 
            FROM temp_denue_wkt;
        """
        con.execute(sql_create_denue)
        print("Tabla 'denue' creada exitosamente desde WKT.")
    else:
        print("ADVERTENCIA: No se encontraron archivos GeoParquet de DENUE.")

    # --- 2. Procesar y Cargar Censo y Manzanas ---
    print("\nPaso 2/3: Creando tabla 'censo_manzanas'...")
    censo_parquet_files = glob.glob(os.path.join(config.CENSO_PARQUET_DIR, '*.parquet'))
    mg_geoparquet_files = glob.glob(os.path.join(config.MARCO_GEO_GEOPARQUET_DIR, '*.geoparquet'))

    if censo_parquet_files and mg_geoparquet_files:
        # Se aplica la misma estrategia de carga robusta (WKT) para las geometrías de las manzanas.
        gdf_manzanas = gpd.read_parquet(mg_geoparquet_files)
        gdf_manzanas['geometry_wkt'] = gdf_manzanas.geometry.to_wkt()
        df_manzanas = gdf_manzanas.drop(columns=['geometry'])
        con.execute("CREATE TEMP TABLE temp_manzanas_wkt AS SELECT * FROM df_manzanas")

        con.execute(f"CREATE TEMP TABLE temp_censo AS SELECT * FROM read_parquet({censo_parquet_files}, union_by_name=True);")
        
        sql_alter_censo = """
            ALTER TABLE temp_censo ADD COLUMN CVEGEO VARCHAR;
            UPDATE temp_censo SET CVEGEO = 
                LPAD(CAST(ENTIDAD AS VARCHAR), 2, '0') ||
                LPAD(CAST(MUN AS VARCHAR), 3, '0') ||
                LPAD(CAST(LOC AS VARCHAR), 4, '0') ||
                AGEB ||
                LPAD(CAST(MZA AS VARCHAR), 3, '0');
        """
        con.execute(sql_alter_censo)

        cols_to_convert = config.CENSO_COLUMNAS_A_INT
        select_expressions = []
        censo_cols_info = {row[0]: row[1] for row in con.execute("DESCRIBE temp_censo;").fetchall()}

        for col in censo_cols_info:
            if col in cols_to_convert:
                expr = f"CASE WHEN c.{col} IN ('N/A', 'N/D', '*', '') THEN NULL ELSE CAST(c.{col} AS INTEGER) END AS {col}"
                select_expressions.append(expr)
            elif col != 'CVEGEO':
                select_expressions.append(f"c.{col}")

        select_clause = ", ".join(select_expressions)

        sql_create_censo_manzanas = f"""
            CREATE TABLE censo_manzanas AS
            SELECT 
                m.CVEGEO,
                ST_GeomFromText(m.geometry_wkt) AS geometry,
                {select_clause}
            FROM temp_manzanas_wkt AS m
            LEFT JOIN temp_censo AS c ON m.CVEGEO = c.CVEGEO;
        """
        con.execute(sql_create_censo_manzanas)
        print("Tabla 'censo_manzanas' creada exitosamente desde WKT.")
    else:
        print("ADVERTENCIA: No se encontraron archivos Parquet de Censo o GeoParquet de Manzanas.")

    # --- 3. Limpieza Final ---
    print("\nPaso 3/3: Limpiando tablas temporales...")
    con.execute("DROP TABLE IF EXISTS temp_denue_wkt;")
    con.execute("DROP TABLE IF EXISTS temp_manzanas_wkt;")
    con.execute("DROP TABLE IF EXISTS temp_censo;")
    con.execute("VACUUM;")
    print("Base de datos finalizada y optimizada.")

    con.close()
    print("--- Construcción de la Base de Datos Finalizada ---")
