from src import denue_processing
from src import censo_processing
from src import database_builder
from src import config
import os

def create_project_directories():
    """Crea todos los directorios necesarios para el proyecto si no existen."""
    print("INFO: Verificando y creando directorios de trabajo...")
    dirs_to_create = [
        config.CENSO_RAW_ZIP_DIR, config.CENSO_CSV_DIR, config.CENSO_PARQUET_DIR,
        config.MARCO_GEO_RAW_ZIP_DIR, config.MARCO_GEO_SHP_DIR, config.MARCO_GEO_GEOPARQUET_DIR,
        config.DENUE_RAW_ZIP_DIR, config.DENUE_SHP_DIR, config.DENUE_GEOPARQUET_DIR,
        os.path.dirname(config.DB_PATH) # Directorio 'output'
    ]
    for directory in dirs_to_create:
        os.makedirs(directory, exist_ok=True)

def main():
    """Función principal que orquesta todo el proceso."""
    print("=================================================================")
    print("=== INICIO DEL PROCESO DE DESCARGA Y CONSTRUCCIÓN DE BBDD ===")
    print("=================================================================")

    # Crear directorios antes de cualquier otra operación
    create_project_directories()

    # Paso 1: Procesar todos los datos del DENUE
    denue_processing.process_denue()

    # Paso 2: Procesar todos los datos del Censo y Marco Geoestadístico
    censo_processing.process_censo_y_marco_geo()

    # Paso 3: Construir la base de datos final con los datos procesados
    database_builder.build_database()

    print("\n==============================================================")
    print("=== PROCESO COMPLETADO EXITOSAMENTE ===")
    print("==============================================================")

if __name__ == "__main__":
    main()
