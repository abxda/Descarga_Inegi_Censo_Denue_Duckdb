# Arquitectura del Proyecto

## 1. Filosofía de Diseño

El proyecto está diseñado siguiendo principios de modularidad y separación de responsabilidades. El objetivo es tener un código limpio, fácil de entender, mantener y extender. Cada parte del proceso (descarga, procesamiento de datos específicos, construcción de la base de datos) está encapsulada en su propio módulo.

## 2. Flujo de Datos

El flujo de datos general sigue estos pasos:

1.  **Descarga**: Los archivos ZIP originales de INEGI se descargan en directorios `raw_zip` específicos para cada fuente de datos (Censo, Marco Geoestadístico, DENUE).
2.  **Extracción**: Los archivos ZIP se descomprimen. Los Shapefiles (`.shp` y archivos asociados) se extraen a las carpetas `shp`.
3.  **Conversión a Formato Intermedio**: 
    - Los archivos `.shp` se convierten a `.geoparquet`. Durante este paso, se realiza la **reproyección a EPSG:4326**.
    - Los archivos `.csv` del censo se convierten a `.parquet` para optimizar la lectura.
4.  **Carga en DuckDB**: Los archivos `.geoparquet` y `.parquet` se utilizan para crear y poblar las tablas en la base de datos DuckDB.
5.  **Transformación en BBDD**: Dentro de DuckDB, se realizan las uniones (`JOIN`) entre los datos censales y las geometrías de manzana, y se limpian los tipos de datos.
6.  **Resultado Final**: Se genera una base de datos DuckDB (`.duckdb`) limpia y lista para el análisis en la carpeta `output/`.

## 3. Descripción de Módulos (Componentes de `src/`)

- **`main.py`**: 
  - Es el orquestador principal del proyecto.
  - Llama a las funciones de los otros módulos en la secuencia correcta para ejecutar el flujo de datos completo.

- **`config.py`**:
  - Centraliza toda la configuración del proyecto.
  - Contiene las URLs base de INEGI, las listas de estados, los nombres de los directorios y las listas de columnas para la limpieza de datos. Esto permite modificar parámetros clave sin alterar la lógica del programa.

- **`download_utils.py`**: 
  - Proporciona funciones genéricas y reutilizables para tareas de descarga y descompresión.
  - `download_file()`: Descarga un archivo desde una URL, verificando si ya existe.
  - `extract_zip()`: Extrae el contenido de un archivo ZIP.

- **`censo_processing.py`**: 
  - Contiene toda la lógica específica para procesar los datos del **Censo de Población y Vivienda 2020** y el **Marco Geoestadístico**.
  - Orquesta la descarga, extracción y conversión a GeoParquet de las manzanas, asegurando la reproyección a EPSG:4326.
  - Maneja la descarga, extracción y conversión a Parquet de los datos tabulares del censo.

- **`denue_processing.py`**: 
  - Contiene la lógica específica para procesar los datos del **DENUE**.
  - Orquesta la descarga, extracción y conversión a GeoParquet de los puntos de unidades económicas, asegurando también la reproyección a EPSG:4326.

- **`database_builder.py`**: 
  - Se encarga de la fase final: la construcción de la base de datos DuckDB.
  - Para evitar problemas de interpretación de geometrías entre librerías, implementa una estrategia robusta:
    1. Lee los archivos GeoParquet con GeoPandas.
    2. Convierte la columna de geometría a su representación de texto **WKT (Well-Known Text)**.
    3. Carga este DataFrame (con la geometría como texto) en una tabla temporal en DuckDB.
    4. Crea la tabla final utilizando la función `ST_GeomFromText()` de la extensión espacial de DuckDB. Esto reconstruye la geometría de forma nativa y correcta a partir del texto WKT, asegurando la máxima compatibilidad.
  - Realiza la unión de los datos del censo con las geometrías de las manzanas.
  - Ejecuta las sentencias SQL para limpiar los tipos de datos (convirtiendo texto a numérico).
  - Consolida las tablas finales (`censo_manzanas` y `denue`).

## 4. Estructura de Directorios `data`

La carpeta `data` está organizada para separar claramente los datos crudos de los procesados, evitando la mezcla de formatos y etapas.

- `data/censo/raw_zip`: Almacena los `.zip` de los datos tabulares del censo.
- `data/censo/csv`: Almacena los `.csv` extraídos.
- `data/censo/parquet`: Almacena los `.parquet` convertidos desde los CSV.

- `data/mg_marco_geo/raw_zip`: Almacena los `.zip` del Marco Geoestadístico.
- `data/mg_marco_geo/shp`: Almacena los Shapefiles extraídos.
- `data/mg_marco_geo/geoparquet`: Almacena los `.geoparquet` convertidos y reproyectados.

- `data/denue/raw_zip`: Almacena los `.zip` del DENUE.
- `data/denue/shp`: Almacena los Shapefiles extraídos.
- `data/denue/geoparquet`: Almacena los `.geoparquet` convertidos y reproyectados.
