import os
import glob
import geopandas as gpd
from . import config
from . import download_utils

def convert_shp_to_geoparquet(shp_path, geoparquet_path):
    """Convierte un Shapefile a GeoParquet, reproyectando a EPSG:4326."""
    if os.path.exists(geoparquet_path):
        #print(f"INFO: GeoParquet ya existe en {geoparquet_path}")
        return

    try:
        #print(f"Convirtiendo {shp_path} a GeoParquet (EPSG:4326)...")
        gdf = gpd.read_file(shp_path, encoding='ISO-8859-1')
        
        # Si el CRS no está definido, asumir el de INEGI. Si está, transformar.
        if gdf.crs is None:
            #print(f"ADVERTENCIA: CRS no definido para {shp_path}. Asumiendo {config.CRS_ORIGEN}.")
            gdf.set_crs(config.CRS_ORIGEN, inplace=True)
        
        gdf = gdf.to_crs(config.CRS_DESTINO)
        gdf.to_parquet(geoparquet_path, index=False)
        #print(f"GeoParquet guardado en: {geoparquet_path}")

    except Exception as e:
        print(f"ERROR al convertir {shp_path}: {e}")

def process_denue():
    """Orquesta la descarga, extracción y conversión de datos del DENUE."""
    print("--- Iniciando Procesamiento de DENUE ---")
    
    # 1. Descargar todos los archivos ZIP del DENUE
    print("Paso 1/3: Descargando archivos ZIP...")
    for url in config.URLS_DENUE:
        download_utils.download_file(url, config.DENUE_RAW_ZIP_DIR)
    
    # 2. Extraer los Shapefiles de cada ZIP
    print("\nPaso 2/3: Extrayendo Shapefiles...")
    zip_files = glob.glob(os.path.join(config.DENUE_RAW_ZIP_DIR, '*.zip'))
    for zip_path in zip_files:
        # El nombre del directorio de extracción será el nombre del zip sin la extensión
        extract_folder_name = os.path.basename(zip_path).replace('.zip', '')
        extract_path = os.path.join(config.DENUE_SHP_DIR, extract_folder_name)
        download_utils.extract_zip(zip_path, extract_path)

    # 3. Convertir todos los Shapefiles a GeoParquet
    print("\nPaso 3/3: Convirtiendo Shapefiles a GeoParquet...")
    shp_files = glob.glob(os.path.join(config.DENUE_SHP_DIR, '**', '*.shp'), recursive=True)
    
    for shp_file in shp_files:
        # Crear un nombre de archivo geoparquet único en el directorio unificado
        base_name = os.path.basename(shp_file).replace('.shp', '.geoparquet')
        geoparquet_path = os.path.join(config.DENUE_GEOPARQUET_DIR, base_name)
        convert_shp_to_geoparquet(shp_file, geoparquet_path)
        
    print("--- Procesamiento de DENUE Finalizado ---")
