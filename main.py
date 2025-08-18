from src import denue_processing
from src import censo_processing
from src import database_builder

def main():
    """Función principal que orquesta todo el proceso."""
    print("=================================================================")
    print("=== INICIO DEL PROCESO DE DESCARGA Y CONSTRUCCIÓN DE BBDD ===")
    print("=================================================================")

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
