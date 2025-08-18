# Diccionario de Datos: Censo y DENUE

Este documento describe las tablas y campos contenidos en la base de datos `censo_denue.duckdb`.

---

## Tabla: `censo_manzanas`

Esta tabla contiene los polígonos de las manzanas urbanas de México, enriquecidos con los indicadores sociodemográficos del Censo de Población y Vivienda 2020 de INEGI.

| Campo | Descripción | Tipo de Dato |
| :--- | :--- | :--- |
| CVEGEO | Clave Geoestadística Única de Manzana, creada por la concatenación de las claves de entidad, municipio, localidad, AGEB y manzana. | VARCHAR |
| geometry | Geometría del polígono de la manzana en proyección EPSG:4326. | GEOMETRY |
| ENTIDAD | Clave de entidad federativa. | BIGINT |
| NOM_ENT | Nombre oficial de la entidad federativa. | VARCHAR |
| MUN | Código que identifica al municipio o demarcación territorial. | BIGINT |
| NOM_MUN | Nombre oficial del municipio o demarcación territorial. | VARCHAR |
| LOC | Código que identifica a la localidad. | BIGINT |
| NOM_LOC | Nombre con el que se reconoce a la localidad. | VARCHAR |
| AGEB | Clave que identifica al AGEB urbana. | VARCHAR |
| MZA | Clave que identifica a la manzana. | BIGINT |
| POBTOT | Población total. | BIGINT |
| POBFEM | Población femenina. | INTEGER |
| POBMAS | Población masculina. | INTEGER |
| P_0A2 | Personas de 0 a 2 años de edad. | INTEGER |
| P_0A2_F | Mujeres de 0 a 2 años de edad. | INTEGER |
| P_0A2_M | Hombres de 0 a 2 años de edad. | INTEGER |
| P_3YMAS | Personas de 3 a 130 años de edad. | INTEGER |
| P_3YMAS_F | Mujeres de 3 a 130 años de edad. | INTEGER |
| P_3YMAS_M | Hombres de 3 a 130 años de edad. | INTEGER |
| P_5YMAS | Personas de 5 a 130 años de edad. | INTEGER |
| P_12YMAS | Personas de 12 a 130 años de edad. | INTEGER |
| P_15YMAS | Personas de 15 a 130 años de edad. | INTEGER |
| P_18YMAS | Personas de 18 a 130 años de edad. | INTEGER |
| P_60YMAS | Personas de 60 a 130 años de edad. | INTEGER |
| PNACOE | Personas nacidas en otra entidad federativa. | INTEGER |
| P3YM_HLI | Personas de 3 a 130 años de edad que hablan alguna lengua indígena. | INTEGER |
| P5_HLI | Personas de 5 a 130 años de edad que hablan alguna lengua indígena. | INTEGER |
| POB_AFRO | Personas que se consideran afromexicanos o afrodescendientes. | INTEGER |
| PCON_DISC | Personas con discapacidad. | INTEGER |
| PCON_LIMI | Personas con limitación en la actividad cotidiana. | INTEGER |
| P15YM_AN | Personas de 15 a 130 años de edad que no saben leer y escribir un recado. | INTEGER |
| P15YM_SE | Personas de 15 a 130 años de edad que no aprobaron ningún grado escolar. | INTEGER |
| GRAPROES | Grado promedio de escolaridad. | INTEGER |
| PEA | Personas de 12 a 130 años de edad que trabajaron, tenían trabajo pero no trabajaron o buscaron trabajo en la semana de referencia. | INTEGER |
| PE_INAC | Personas de 12 a 130 años de edad no económicamente activas. | INTEGER |
| POCUPADA | Personas de 12 a 130 años de edad que trabajaron o que no trabajaron, pero sí tenían trabajo en la semana de referencia. | INTEGER |
| PDESOCUP | Personas de 12 a 130 años de edad que no tenían trabajo, pero buscaron trabajo en la semana de referencia. | INTEGER |
| PSINDER | Total de personas que no están afiliadas a servicios médicos en ninguna institución pública o privada. | INTEGER |
| PDER_SS | Total de personas que están afiliadas a servicios médicos en alguna institución de salud pública o privada. | INTEGER |
| VIVTOT | Viviendas particulares habitadas, deshabitadas, de uso temporal y colectivas. | BIGINT |
| TVIVHAB | Viviendas particulares y colectivas habitadas. | INTEGER |
| VIVPAR_HAB | Viviendas particulares habitadas de cualquier clase. | INTEGER |
| OCUPVIVPAR | Personas que residen en viviendas particulares habitadas. | INTEGER |
| PROM_OCUP | Promedio de ocupantes en viviendas particulares habitadas. | INTEGER |
| VPH_PISOTI | Viviendas particulares habitadas con piso de tierra. | INTEGER |
| VPH_1DOR | Viviendas particulares habitadas con un dormitorio. | INTEGER |
| VPH_C_ELEC | Viviendas particulares habitadas que tienen energía eléctrica. | INTEGER |
| VPH_AGUADV | Viviendas particulares habitadas que tienen disponibilidad de agua entubada. | INTEGER |
| VPH_DRENAJ | Viviendas particulares habitadas que tienen drenaje. | INTEGER |
| VPH_REFRI | Viviendas particulares habitadas que tienen refrigerador. | INTEGER |
| VPH_LAVAD | Viviendas particulares habitadas que tienen lavadora. | INTEGER |
| VPH_HMICRO | Viviendas particulares habitadas que tienen horno de microondas. | INTEGER |
| VPH_AUTOM | Viviendas particulares habitadas que tienen automóvil o camioneta. | INTEGER |
| VPH_MOTO | Viviendas particulares habitadas que tienen motocicleta o motoneta. | INTEGER |
| VPH_BICI | Viviendas particulares habitadas que tienen bicicleta que se utilice como medio de transporte. | INTEGER |
| VPH_RADIO | Viviendas particulares habitadas que tienen algún aparato o dispositivo para oír radio. | INTEGER |
| VPH_TV | Viviendas particulares habitadas que tienen televisor. | INTEGER |
| VPH_PC | Viviendas particulares habitadas que tienen computadora, laptop o tablet. | INTEGER |
| VPH_TELEF | Viviendas particulares habitadas que tienen línea telefónica fija. | INTEGER |
| VPH_CEL | Viviendas particulares habitadas que tienen teléfono celular. | INTEGER |
| VPH_INTER | Viviendas particulares habitadas que tienen Internet. | INTEGER |
| VPH_STVP | Viviendas particulares habitadas que tienen servicio de televisión de paga (cable o satelital). | INTEGER |
| VPH_SPMVPI | Viviendas particulares habitadas que tienen servicio de películas, música o videos de paga por Internet. | INTEGER |
| VPH_CVJ | Viviendas particulares habitadas que tienen consola de videojuegos. | INTEGER |
*Nota: Se presenta una selección de los campos más relevantes. La tabla completa contiene más de 200 indicadores detallados en el diccionario de datos oficial de INEGI.*

---

## Tabla: `denue`

Esta tabla contiene los puntos de todas las unidades económicas del Directorio Estadístico Nacional de Unidades Económicas (DENUE) de INEGI.

| Campo | Descripción | Tipo de Dato |
| :--- | :--- | :--- |
| id | Número de identificación del DENUE, es una clave numérica única. | INTEGER |
| clee | Llave única de identificación estadística, asignada por el INEGI. | VARCHAR |
| nom_estab | Nombre comercial o exterior con el que se identifica la unidad económica. | VARCHAR |
| raz_social | Forma con que está legalmente constituida y registrada la persona moral. | VARCHAR |
| codigo_act | Código de actividad basado en el Sistema de Clasificación Industrial para América del Norte (SCIAN). | VARCHAR |
| nombre_act | Nombre del código de actividad conforme al SCIAN. | VARCHAR |
| per_ocu | Rango del personal ocupado total. | VARCHAR |
| tipo_vial | Tipo de vialidad (calle, avenida, andador, etc.). | VARCHAR |
| nom_vial | Nombre de la vialidad. | VARCHAR |
| numero_ext | Número exterior del inmueble. | VARCHAR |
| letra_ext | Letra exterior del inmueble. | VARCHAR |
| edificio | Nombre del edificio donde se ubica la unidad económica. | VARCHAR |
| num_local | Dato alfanumérico que corresponde al local. | VARCHAR |
| tipo_asent | Tipo de asentamiento humano (colonia, fraccionamiento, etc.). | VARCHAR |
| nomb_asent | Nombre del asentamiento humano. | VARCHAR |
| cod_postal | Código Postal de 5 dígitos. | VARCHAR |
| cve_ent | Clave de la entidad federativa. | VARCHAR |
| entidad | Nombre de la entidad federativa. | VARCHAR |
| cve_mun | Clave del municipio. | VARCHAR |
| municipio | Nombre del municipio. | VARCHAR |
| cve_loc | Clave de la localidad. | VARCHAR |
| localidad | Nombre de la localidad. | VARCHAR |
| ageb | Clave del Área Geoestadística Básica (AGEB). | VARCHAR |
| manzana | Clave geoestadística de la manzana. | VARCHAR |
| telefono | Número telefónico de la unidad económica. | VARCHAR |
| correoelec | Correo electrónico de la unidad económica. | VARCHAR |
| www | Página web de la unidad económica. | VARCHAR |
| tipoUniEco | Identifica si el establecimiento es Fijo o Semifijo. | VARCHAR |
| latitud | Distancia entre la unidad económica y el ecuador (coordenada original). | DOUBLE |
| longitud | Distancia entre la unidad económica y el meridiano de Greenwich (coordenada original). | DOUBLE |
| fecha_alta | Fecha en la que la unidad económica se integró al directorio. | VARCHAR |
| geometry_wkt | Geometría en formato Well-Known Text, usada para la carga de datos. | VARCHAR |
| geometry | Geometría del punto de la unidad económica en proyección EPSG:4326. | GEOMETRY |
