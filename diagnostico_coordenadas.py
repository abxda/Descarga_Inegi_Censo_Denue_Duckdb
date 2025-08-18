import geopandas as gpd
import os
from shapely.ops import transform

# --- Configuración ---
ESTADO_PRUEBA = "01"
GEOPARQUET_MANZANAS_DIR = "data/mg_marco_geo/geoparquet/"

# --- Funciones ---
def swap_xy(geom):
    """Intercambia las coordenadas X e Y de una geometría shapely."""
    return transform(lambda x, y, z=None: (y, x, z), geom)

# --- Script de Diagnóstico ---
print("--- Iniciando Script de Diagnóstico de Coordenadas ---")

archivo_prueba_path = os.path.join(GEOPARQUET_MANZANAS_DIR, f"{ESTADO_PRUEBA}_manzanas.geoparquet")

if not os.path.exists(archivo_prueba_path):
    print(f"ERROR: No se encontró el archivo de prueba: {archivo_prueba_path}")
else:
    print(f"Analizando archivo: {archivo_prueba_path}")
    gdf = gpd.read_parquet(archivo_prueba_path)
    primera_geometria = gdf.geometry.iloc[0]
    centroide = primera_geometria.centroid

    print("\n--- Resultados del Análisis Original ---")
    print(f"Proyección del archivo (CRS): {gdf.crs}")
    print(f"Coordenadas del centroide ORIGINAL:")
    print(f"  - X: {centroide.x}")
    print(f"  - Y: {centroide.y}")

    # Guardar el punto original para comparación
    output_geojson_original = "punto_de_prueba_original.geojson"
    gpd.GeoDataFrame([{'id': 1}], geometry=[centroide], crs=gdf.crs).to_file(output_geojson_original, driver='GeoJSON')
    print(f"\nSe generó '\033[1m{output_geojson_original}\033[0m' (en el Océano Índico). ")

    # --- Aplicar Corrección ---
    print("\n--- Aplicando Corrección (Intercambio X-Y) ---")
    centroide_corregido = swap_xy(centroide)
    print(f"Coordenadas del centroide CORREGIDO:")
    print(f"  - X (Longitud ahora): {centroide_corregido.x}")
    print(f"  - Y (Latitud ahora):  {centroide_corregido.y}")

    # Guardar el punto corregido
    output_geojson_corregido = "punto_de_prueba_corregido.geojson"
    gpd.GeoDataFrame([{'id': 1}], geometry=[centroide_corregido], crs=gdf.crs).to_file(output_geojson_corregido, driver='GeoJSON')
    print(f"\nSe ha generado un segundo archivo: '\033[1m{output_geojson_corregido}\033[0m'.")
    print("\033[1mPor favor, verifica si este nuevo punto SÍ aparece en la ubicación correcta en México.\033[0m")

print("\n--- Diagnóstico Finalizado ---")