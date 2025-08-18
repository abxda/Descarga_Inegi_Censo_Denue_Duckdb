# Proyecto de Descarga y Procesamiento de Datos INEGI: Censo 2020 y DENUE

## 1. Descripción General

Este proyecto automatiza el proceso de descarga, procesamiento y consolidación de datos geoespaciales del Censo de Población y Vivienda 2020 y del Directorio Estadístico Nacional de Unidades Económicas (DENUE) del INEGI.

El objetivo final es generar una base de datos **DuckDB** optimizada que contenga dos tablas principales listas para el análisis geoespacial:
1.  `censo_manzanas`: Polígonos de manzanas urbanas de todo México, enriquecidos con los indicadores sociodemográficos del Censo 2020.
2.  `denue`: Puntos geográficos de todas las unidades económicas del DENUE.

Todas las geometrías en la base de datos final están estandarizadas en la proyección **EPSG:4326 (WGS 84)**.

## 2. Características Principales

- **Modularidad**: El código está organizado en módulos para facilitar su mantenimiento y extensibilidad.
- **Eficiencia**: Utiliza `geoparquet` como formato intermedio para acelerar las operaciones de lectura/escritura geoespacial.
- **Inteligente**: El script verifica si los archivos ya han sido descargados antes de iniciar una nueva descarga, ahorrando tiempo y ancho de banda.
- **Reproyección Automática**: Corrige la proyección de los datos del Marco Geoestadístico de INEGI a EPSG:4326.
- **Limpieza de Datos**: Maneja y limpia los valores no numéricos (ej. `*`, `N/D`) de los datos censales para convertirlos a tipos de datos numéricos adecuados.

## 3. Requisitos

- Python 3.8 o superior
- Un entorno virtual (recomendado)

## 4. Instrucciones de Uso

1.  **Clonar el repositorio (o descargar los archivos en la estructura generada) y navegar al directorio:**
    ```bash
    # Reemplaza <URL_DEL_REPOSITORIO> con la URL real si clonas el proyecto
    # git clone <URL_DEL_REPOSITORIO>
    cd Descarga_Inegi_Censo_Denue_Duckdb
    ```

2.  **Crear y activar un entorno virtual:**
    - En macOS y Linux:
      ```bash
      python3 -m venv env
      source env/bin/activate
      ```
    - En Windows:
      ```bash
      python -m venv env
      .\env\Scripts\activate
      ```

3.  **Instalar las dependencias:**
    Una vez que el entorno virtual esté activado, instala las librerías necesarias desde el archivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar el script principal:**
    Una vez que el script finalice, encontrarás la base de datos en la siguiente ruta:
    `output/censo_denue.duckdb`

## 5. Estructura del Proyecto

```
Descarga_Inegi_Censo_Denue_Duckdb/
├── data/             # Archivos intermedios y descargados
├── output/           # Base de datos final
├── src/              # Código fuente modular
│   ├── censo_processing.py
│   ├── config.py
│   ├── database_builder.py
│   ├── denue_processing.py
│   └── download_utils.py
├── .gitignore
├── ARQUITECTURA.md   # Documentación de la arquitectura
├── main.py           # Script principal para ejecutar el proceso
└── README.md         # Este archivo
```
