import os
import glob
import duckdb
from . import config

def build_database():
    """Crea y puebla la base de datos DuckDB con los datos procesados."""
    print("--- Iniciando Construcción de la Base de Datos DuckDB ---")

    # Eliminar la base de datos anterior si existe
    if os.path.exists(config.DB_PATH):
        os.remove(config.DB_PATH)
        print(f"INFO: Base de datos anterior eliminada en {config.DB_PATH}")

    con = duckdb.connect(config.DB_PATH)
    con.execute("INSTALL spatial; LOAD spatial;")

    # --- 1. Procesar y Cargar DENUE ---
    print("\nPaso 1/3: Creando tabla 'denue'...")
    denue_geoparquet_files = glob.glob(os.path.join(config.DENUE_GEOPARQUET_DIR, '*.geoparquet'))
    if denue_geoparquet_files:
        # DuckDB puede leer una lista de archivos parquet directamente
        con.execute(f"CREATE TABLE denue AS SELECT * FROM read_parquet({denue_geoparquet_files}, union_by_name=True);")
        print("Tabla 'denue' creada exitosamente.")
    else:
        print("ADVERTENCIA: No se encontraron archivos GeoParquet de DENUE.")

    # --- 2. Procesar y Cargar Censo y Manzanas ---
    print("\nPaso 2/3: Creando tabla 'censo_manzanas'...")
    censo_parquet_files = glob.glob(os.path.join(config.CENSO_PARQUET_DIR, '*.parquet'))
    mg_geoparquet_files = glob.glob(os.path.join(config.MARCO_GEO_GEOPARQUET_DIR, '*.geoparquet'))

    if censo_parquet_files and mg_geoparquet_files:
        # Crear tablas temporales para censo y manzanas
        con.execute(f"CREATE OR REPLACE TEMP TABLE temp_censo AS SELECT * FROM read_parquet({censo_parquet_files}, union_by_name=True);")
        con.execute(f"CREATE OR REPLACE TEMP TABLE temp_manzanas AS SELECT * FROM read_parquet({mg_geoparquet_files}, union_by_name=True);")

        # Construir la clave CVEGEO en la tabla de censo
        con.execute("""
            ALTER TABLE temp_censo ADD COLUMN CVEGEO VARCHAR;
            UPDATE temp_censo SET CVEGEO = 
                LPAD(CAST(ENTIDAD AS VARCHAR), 2, '0') ||
                LPAD(CAST(MUN AS VARCHAR), 3, '0') ||
                LPAD(CAST(LOC AS VARCHAR), 4, '0') ||
                AGEB ||
                LPAD(CAST(MZA AS VARCHAR), 3, '0');
        """)

        # Construir la expresión CASE para la conversión de tipos de datos
        cols_to_convert = config.CENSO_COLUMNAS_A_INT
        select_expressions = []
        
        # Obtener columnas de la tabla de censo para evitar errores si alguna no existe
        censo_cols_info = {row[0]: row[1] for row in con.execute("DESCRIBE temp_censo;").fetchall()}

        for col in censo_cols_info:
            if col in cols_to_convert:
                # Expresión para convertir a INTEGER, manejando nulos
                expr = f"CASE WHEN c.{col} IN ('N/A', 'N/D', '*', '') THEN NULL ELSE CAST(c.{col} AS INTEGER) END AS {col}"
                select_expressions.append(expr)
            elif col != 'CVEGEO': # Evitar duplicar CVEGEO
                select_expressions.append(f"c.{col}")

        select_clause = ", ".join(select_expressions)

        # Crear la tabla final uniendo censo y manzanas, y aplicando la limpieza
        con.execute(f"""
            CREATE TABLE censo_manzanas AS
            SELECT 
                m.CVEGEO,
                m.geometry,
                {select_clause}
            FROM temp_manzanas AS m
            LEFT JOIN temp_censo AS c ON m.CVEGEO = c.CVEGEO;
        """)
        print("Tabla 'censo_manzanas' creada exitosamente.")
    else:
        print("ADVERTENCIA: No se encontraron archivos Parquet de Censo o GeoParquet de Manzanas.")

    # --- 3. Limpieza Final ---
    print("\nPaso 3/3: Limpiando tablas temporales...")
    con.execute("DROP TABLE IF EXISTS temp_censo;")
    con.execute("DROP TABLE IF EXISTS temp_manzanas;")
    con.execute("VACUUM;")
    print("Base de datos finalizada y optimizada.")

    con.close()
    print("--- Construcción de la Base de Datos Finalizada ---")
