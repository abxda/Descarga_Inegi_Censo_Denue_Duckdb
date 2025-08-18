import os
import glob
import pandas as pd
import geopandas as gpd
from . import config
from . import download_utils

def convert_censo_csv_to_parquet(csv_path, parquet_path):
    """Convierte un CSV del censo a Parquet, manejando la codificación."""
    if os.path.exists(parquet_path):
        #print(f"INFO: Parquet ya existe en {parquet_path}")
        return

    try:
        #print(f"Convirtiendo {csv_path} a Parquet...")
        # Intentar con UTF-8, si falla, usar ISO-8859-1
        try:
            df = pd.read_csv(csv_path, low_memory=False, encoding='utf-8')
        except UnicodeDecodeError:
            #print(f"ADVERTENCIA: Falló la lectura de {csv_path} con UTF-8. Reintentando con ISO-8859-1.")
            df = pd.read_csv(csv_path, low_memory=False, encoding='ISO-8859-1')
        
        df.to_parquet(parquet_path, index=False)
        #print(f"Parquet guardado en: {parquet_path}")

    except Exception as e:
        print(f"ERROR al convertir {csv_path} a Parquet: {e}")

def convert_mg_shp_to_geoparquet(shp_path, geoparquet_path):
    """Convierte un Shapefile del Marco Geoestadístico a GeoParquet, reproyectando."""
    if os.path.exists(geoparquet_path):
        #print(f"INFO: GeoParquet ya existe en {geoparquet_path}")
        return

    try:
        #print(f"Convirtiendo {shp_path} a GeoParquet (EPSG:4326)...")
        gdf = gpd.read_file(shp_path, encoding='ISO-8859-1')
        
        if gdf.crs is None:
            #print(f"ADVERTENCIA: CRS no definido para {shp_path}. Asumiendo {config.CRS_ORIGEN}.")
            gdf.set_crs(config.CRS_ORIGEN, inplace=True)
        
        gdf = gdf.to_crs(config.CRS_DESTINO)
        gdf.to_parquet(geoparquet_path, index=False)
        #print(f"GeoParquet guardado en: {geoparquet_path}")

    except Exception as e:
        print(f"ERROR al convertir {shp_path}: {e}")

def process_censo_y_marco_geo():
    """Orquesta la descarga y procesamiento de datos del Censo y Marco Geoestadístico."""
    print("--- Iniciando Procesamiento de Censo y Marco Geoestadístico ---")

    # Iterar por cada estado para procesar sus datos
    for num, geo_zip_name in zip(config.ESTADOS_NUM, config.ESTADOS_GEO):
        estado_str = f"{num:02d}"
        print(f"\nProcesando Estado {estado_str}...")

        # --- 1. Procesamiento del Marco Geoestadístico (Geometrías) ---
        mg_url = config.BASE_URL_MARCO_GEO + geo_zip_name
        mg_zip_path = download_utils.download_file(mg_url, config.MARCO_GEO_RAW_ZIP_DIR)
        
        if mg_zip_path:
            # Extraer solo los archivos de manzana (*m.shp, etc.)
            cod = geo_zip_name.split('_')[0]
            shape_type = "m" # Manzanas
            shp_files_to_extract = [
                f'conjunto_de_datos/{cod}{shape_type}.shp',
                f'conjunto_de_datos/{cod}{shape_type}.cpg',
                f'conjunto_de_datos/{cod}{shape_type}.dbf',
                f'conjunto_de_datos/{cod}{shape_type}.prj',
                f'conjunto_de_datos/{cod}{shape_type}.shx'
            ]
            mg_extract_path = os.path.join(config.MARCO_GEO_SHP_DIR, estado_str)
            download_utils.extract_zip(mg_zip_path, mg_extract_path, specific_files=shp_files_to_extract)

            # Convertir el shapefile extraído a GeoParquet
            shp_path = os.path.join(mg_extract_path, 'conjunto_de_datos', f'{cod}{shape_type}.shp')
            if os.path.exists(shp_path):
                geoparquet_path = os.path.join(config.MARCO_GEO_GEOPARQUET_DIR, f'{estado_str}_manzanas.geoparquet')
                convert_mg_shp_to_geoparquet(shp_path, geoparquet_path)

        # --- 2. Procesamiento de Datos del Censo (CSV) ---
        censo_zip_name = f"ageb_mza_urbana_{estado_str}_cpv2020_csv.zip"
        censo_url = config.BASE_URL_CENSO_CSV + censo_zip_name
        censo_zip_path = download_utils.download_file(censo_url, config.CENSO_RAW_ZIP_DIR)

        if censo_zip_path:
            # Construir la ruta relativa esperada del archivo CSV de datos principal.
            # Se usa / porque el estándar ZIP siempre usa forward slashes, independientemente del SO.
            folder_in_zip = f"ageb_mza_urbana_{estado_str}_cpv2020"
            csv_in_zip = f"conjunto_de_datos/conjunto_de_datos_ageb_urbana_{estado_str}_cpv2020.csv"
            csv_path_in_zip = f"{folder_in_zip}/{csv_in_zip}"

            # Extraer únicamente el archivo CSV de datos
            download_utils.extract_zip(censo_zip_path, config.CENSO_CSV_DIR, specific_files=[csv_path_in_zip])
            
            # Convertir el CSV extraído a Parquet
            extracted_csv_path = os.path.join(config.CENSO_CSV_DIR, csv_path_in_zip)
            if os.path.exists(extracted_csv_path):
                parquet_path = os.path.join(config.CENSO_PARQUET_DIR, f'{estado_str}_censo.parquet')
                convert_censo_csv_to_parquet(extracted_csv_path, parquet_path)

    print("\n--- Procesamiento de Censo y Marco Geoestadístico Finalizado ---")
