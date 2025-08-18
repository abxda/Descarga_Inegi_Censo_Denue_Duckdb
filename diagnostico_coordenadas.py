import geopandas as gpd
import os

# --- Configuración ---
ESTADO_PRUEBA = "01"
SHP_DIR = "data/mg_marco_geo/shp/"
CRS_ORIGEN = "EPSG:6372"
CRS_DESTINO = "EPSG:4326"

# --- Script de Diagnóstico ---
print("---" + "Iniciando Diagnóstico: Verificación de Reproyección" + "---")

# 1. Construir la ruta al Shapefile original
shp_path = os.path.join(SHP_DIR, ESTADO_PRUEBA, 'conjunto_de_datos', f'{ESTADO_PRUEBA}m.shp')

if not os.path.exists(shp_path):
    print(f"ERROR: No se encontró el Shapefile original en: {shp_path}")
else:
    print(f"Paso 1: Leyendo 10 manzanas del Shapefile original: {shp_path}")
    gdf_original = gpd.read_file(shp_path).head(10)
    print(f" -> CRS Original: {gdf_original.crs}")

    # --- Guardar muestra sin reproyectar (como referencia) ---
    # gdf_original.to_file("diagnostico_10_manzanas_originales.geojson", driver='GeoJSON')

    # ---------------------------------------------------
    print(f"\nPaso 2: Reproyectando de {CRS_ORIGEN} a {CRS_DESTINO}...")
    
    # Aplicar la reproyección
    gdf_reproyectado = gdf_original.to_crs(CRS_DESTINO)
    
    print(" -> Reproyección completada.")
    
    # Analizar el centroide de la primera manzana DESPUÉS de reproyectar
    centroide_reproyectado = gdf_reproyectado.geometry.iloc[0].centroid
    print("\nCoordenadas del centroide de la primera manzana (después de reproyectar):")
    print(f"  - X (Longitud): {centroide_reproyectado.x}")
    print(f"  - Y (Latitud):  {centroide_reproyectado.y}")
    # ---------------------------------------------------

    # 3. Guardar el resultado reproyectado para verificación visual
    output_geojson = "diagnostico_10_manzanas_REPROYECTADAS.geojson"
    gdf_reproyectado.to_file(output_geojson, driver='GeoJSON')

    print(f"\nPaso 3: Archivo de resultado generado: '\033[1m{output_geojson}\033[0m'.")
    print("\033[1mPor favor, abre este NUEVO archivo en QGIS.")
    print("Verifica si este archivo presenta el problema de 'espejo' o 'volteado'.\033[0m")

print("\n---" + "Diagnóstico Finalizado" + "---")