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
| P_0A2 | Población de 0 a 2 años. | INTEGER |
| P_0A2_F | Población femenina de 0 a 2 años. | INTEGER |
| P_0A2_M | Población masculina de 0 a 2 años. | INTEGER |
| P_3YMAS | Población de 3 años y más. | INTEGER |
| P_3YMAS_F | Población femenina de 3 años y más. | INTEGER |
| P_3YMAS_M | Población masculina de 3 años y más. | INTEGER |
| P_5YMAS | Población de 5 años y más. | INTEGER |
| P_5YMAS_F | Población femenina de 5 años y más. | INTEGER |
| P_5YMAS_M | Población masculina de 5 años y más. | INTEGER |
| P_12YMAS | Población de 12 años y más. | INTEGER |
| P_12YMAS_F | Población femenina de 12 años y más. | INTEGER |
| P_12YMAS_M | Población masculina de 12 años y más. | INTEGER |
| P_15YMAS | Población de 15 años y más. | INTEGER |
| P_15YMAS_F | Población femenina de 15 años y más. | INTEGER |
| P_15YMAS_M | Población masculina de 15 años y más. | INTEGER |
| P_18YMAS | Población de 18 años y más. | INTEGER |
| P_18YMAS_F | Población femenina de 18 años y más. | INTEGER |
| P_18YMAS_M | Población masculina de 18 años y más. | INTEGER |
| P_3A5 | Población de 3 a 5 años. | INTEGER |
| P_3A5_F | Población femenina de 3 a 5 años. | INTEGER |
| P_3A5_M | Población masculina de 3 a 5 años. | INTEGER |
| P_6A11 | Población de 6 a 11 años. | INTEGER |
| P_6A11_F | Población femenina de 6 a 11 años. | INTEGER |
| P_6A11_M | Población masculina de 6 a 11 años. | INTEGER |
| P_8A14 | Población de 8 a 14 años. | INTEGER |
| P_8A14_F | Población femenina de 8 a 14 años. | INTEGER |
| P_8A14_M | Población masculina de 8 a 14 años. | INTEGER |
| P_12A14 | Población de 12 a 14 años. | INTEGER |
| P_12A14_F | Población femenina de 12 a 14 años. | INTEGER |
| P_12A14_M | Población masculina de 12 a 14 años. | INTEGER |
| P_15A17 | Población de 15 a 17 años. | INTEGER |
| P_15A17_F | Población femenina de 15 a 17 años. | INTEGER |
| P_15A17_M | Población masculina de 15 a 17 años. | INTEGER |
| P_18A24 | Población de 18 a 24 años. | INTEGER |
| P_18A24_F | Población femenina de 18 a 24 años. | INTEGER |
| P_18A24_M | Población masculina de 18 a 24 años. | INTEGER |
| P_15A49_F | Población femenina de 15 a 49 años. | INTEGER |
| P_60YMAS | Población de 60 años y más. | INTEGER |
| P_60YMAS_F | Población femenina de 60 años y más. | INTEGER |
| P_60YMAS_M | Población masculina de 60 años y más. | INTEGER |
| REL_H_M | Relación hombres-mujeres. | INTEGER |
| POB0_14 | Población de 0 a 14 años. | INTEGER |
| POB15_64 | Población de 15 a 64 años. | INTEGER |
| POB65_MAS | Población de 65 años y más. | INTEGER |
| PROM_HNV | Promedio de hijas e hijos nacidos vivos. | INTEGER |
| PNACENT | Población nacida en la entidad. | INTEGER |
| PNACENT_F | Población femenina nacida en la entidad. | INTEGER |
| PNACENT_M | Población masculina nacida en la entidad. | INTEGER |
| PNACOE | Población nacida en otra entidad. | INTEGER |
| PNACOE_F | Población femenina nacida en otra entidad. | INTEGER |
| PNACOE_M | Población masculina nacida en otra entidad. | INTEGER |
| PRES2015 | Población de 5 años y más residente en la entidad en marzo de 2015. | INTEGER |
| PRES2015_F | Población femenina de 5 años y más residente en la entidad en marzo de 2015. | INTEGER |
| PRES2015_M | Población masculina de 5 años y más residente en la entidad en marzo de 2015. | INTEGER |
| PRESOE15 | Población de 5 años y más residente en otra entidad en marzo de 2015. | INTEGER |
| PRESOE15_F | Población femenina de 5 años y más residente en otra entidad en marzo de 2015. | INTEGER |
| PRESOE15_M | Población masculina de 5 años y más residente en otra entidad en marzo de 2015. | INTEGER |
| P3YM_HLI | Población de 3 años y más que habla alguna lengua indígena. | INTEGER |
| P3YM_HLI_F | Población femenina de 3 años y más que habla alguna lengua indígena. | INTEGER |
| P3YM_HLI_M | Población masculina de 3 años y más que habla alguna lengua indígena. | INTEGER |
| P3HLINHE | Población de 3 años y más que habla alguna lengua indígena y no habla español. | INTEGER |
| P3HLINHE_F | Población femenina de 3 años y más que habla alguna lengua indígena y no habla español. | INTEGER |
| P3HLINHE_M | Población masculina de 3 años y más que habla alguna lengua indígena y no habla español. | INTEGER |
| P3HLI_HE | Población de 3 años y más que habla alguna lengua indígena y habla español. | INTEGER |
| P3HLI_HE_F | Población femenina de 3 años y más que habla alguna lengua indígena y habla español. | INTEGER |
| P3HLI_HE_M | Población masculina de 3 años y más que habla alguna lengua indígena y habla español. | INTEGER |
| P5_HLI | Población de 5 años y más que habla alguna lengua indígena. | INTEGER |
| P5_HLI_NHE | Población de 5 años y más que habla alguna lengua indígena y no habla español. | INTEGER |
| P5_HLI_HE | Población de 5 años y más que habla alguna lengua indígena y habla español. | INTEGER |
| PHOG_IND | Población en hogares censales indígenas. | INTEGER |
| POB_AFRO | Población que se considera afromexicana o afrodescendiente. | INTEGER |
| POB_AFRO_F | Población femenina que se considera afromexicana o afrodescendiente. | INTEGER |
| POB_AFRO_M | Población masculina que se considera afromexicana o afrodescendiente. | INTEGER |
| PCON_DISC | Población con discapacidad. | INTEGER |
| PCDISC_MOT | Población con discapacidad para caminar, subir o bajar. | INTEGER |
| PCDISC_VIS | Población con discapacidad para ver, aun usando lentes. | INTEGER |
| PCDISC_LENG | Población con discapacidad para hablar o comunicarse. | INTEGER |
| PCDISC_AUD | Población con discapacidad para oír, aun usando aparato auditivo. | INTEGER |
| PCDISC_MOT2 | Población con discapacidad para vestirse, bañarse o comer. | INTEGER |
| PCDISC_MEN | Población con discapacidad para recordar o concentrarse. | INTEGER |
| PCON_LIMI | Población con limitación. | INTEGER |
| PCLIM_CSB | Población con limitación para caminar, subir o bajar. | INTEGER |
| PCLIM_VIS | Población con limitación para ver, aun usando lentes. | INTEGER |
| PCLIM_HACO | Población con limitación para hablar o comunicarse. | INTEGER |
| PCLIM_OAUD | Población con limitación para oír, aun usando aparato auditivo. | INTEGER |
| PCLIM_MOT2 | Población con limitación para vestirse, bañarse o comer. | INTEGER |
| PCLIM_RE_CO | Población con limitación para recordar o concentrarse. | INTEGER |
| PCLIM_PMEN | Población con algún problema o condición mental. | INTEGER |
| PSIND_LIM | Población sin discapacidad, limitación, problema o condición mental. | INTEGER |
| P3A5_NOA | Población de 3 a 5 años que no asiste a la escuela. | INTEGER |
| P3A5_NOA_F | Población femenina de 3 a 5 años que no asiste a la escuela. | INTEGER |
| P3A5_NOA_M | Población masculina de 3 a 5 años que no asiste a la escuela. | INTEGER |
| P6A11_NOA | Población de 6 a 11 años que no asiste a la escuela. | INTEGER |
| P6A11_NOAF | Población femenina de 6 a 11 años que no asiste a la escuela. | INTEGER |
| P6A11_NOAM | Población masculina de 6 a 11 años que no asiste a la escuela. | INTEGER |
| P12A14NOA | Población de 12 a 14 años que no asiste a la escuela. | INTEGER |
| P12A14NOAF | Población femenina de 12 a 14 años que no asiste a la escuela. | INTEGER |
| P12A14NOAM | Población masculina de 12 a 14 años que no asiste a la escuela. | INTEGER |
| P15A17A | Población de 15 a 17 años que asiste a la escuela. | INTEGER |
| P15A17A_F | Población femenina de 15 a 17 años que asiste a la escuela. | INTEGER |
| P15A17A_M | Población masculina de 15 a 17 años que asiste a la escuela. | INTEGER |
| P18A24A | Población de 18 a 24 años que asiste a la escuela. | INTEGER |
| P18A24A_F | Población femenina de 18 a 24 años que asiste a la escuela. | INTEGER |
| P18A24A_M | Población masculina de 18 a 24 años que asiste a la escuela. | INTEGER |
| P8A14AN | Población de 8 a 14 años que no sabe leer y escribir. | INTEGER |
| P8A14AN_F | Población femenina de 8 a 14 años que no sabe leer y escribir. | INTEGER |
| P8A14AN_M | Población masculina de 8 a 14 años que no sabe leer y escribir. | INTEGER |
| P15YM_AN | Población de 15 años y más analfabeta. | INTEGER |
| P15YM_AN_F | Población femenina de 15 años y más analfabeta. | INTEGER |
| P15YM_AN_M | Población masculina de 15 años y más analfabeta. | INTEGER |
| P15YM_SE | Población de 15 años y más sin escolaridad. | INTEGER |
| P15YM_SE_F | Población femenina de 15 años y más sin escolaridad. | INTEGER |
| P15YM_SE_M | Población masculina de 15 años y más sin escolaridad. | INTEGER |
| P15PRI_IN | Población de 15 años y más con primaria incompleta. | INTEGER |
| P15PRI_INF | Población femenina de 15 años y más con primaria incompleta. | INTEGER |
| P15PRI_INM | Población masculina de 15 años y más con primaria incompleta. | INTEGER |
| P15PRI_CO | Población de 15 años y más con primaria completa. | INTEGER |
| P15PRI_COF | Población femenina de 15 años y más con primaria completa. | INTEGER |
| P15PRI_COM | Población masculina de 15 años y más con primaria completa. | INTEGER |
| P15SEC_IN | Población de 15 años y más con secundaria incompleta. | INTEGER |
| P15SEC_INF | Población femenina de 15 años y más con secundaria incompleta. | INTEGER |
| P15SEC_INM | Población masculina de 15 años y más con secundaria incompleta. | INTEGER |
| P15SEC_CO | Población de 15 años y más con secundaria completa. | INTEGER |
| P15SEC_COF | Población femenina de 15 años y más con secundaria completa. | INTEGER |
| P15SEC_COM | Población masculina de 15 años y más con secundaria completa. | INTEGER |
| P18YM_PB | Población de 18 años y más con educación posbásica. | INTEGER |
| P18YM_PB_F | Población femenina de 18 años y más con educación posbásica. | INTEGER |
| P18YM_PB_M | Población masculina de 18 años y más con educación posbásica. | INTEGER |
| GRAPROES | Grado promedio de escolaridad. | INTEGER |
| GRAPROES_F | Grado promedio de escolaridad de la población femenina. | INTEGER |
| GRAPROES_M | Grado promedio de escolaridad de la población masculina. | INTEGER |
| PEA | Población de 12 años y más económicamente activa. | INTEGER |
| PEA_F | Población femenina de 12 años y más económicamente activa. | INTEGER |
| PEA_M | Población masculina de 12 años y más económicamente activa. | INTEGER |
| PE_INAC | Población de 12 años y más no económicamente activa. | INTEGER |
| PE_INAC_F | Población femenina de 12 años y más no económicamente activa. | INTEGER |
| PE_INAC_M | Población masculina de 12 años y más no económicamente activa. | INTEGER |
| POCUPADA | Población de 12 años y más ocupada. | INTEGER |
| POCUPADA_F | Población femenina de 12 años y más ocupada. | INTEGER |
| POCUPADA_M | Población masculina de 12 años y más ocupada. | INTEGER |
| PDESOCUP | Población de 12 años y más desocupada. | INTEGER |
| PDESOCUP_F | Población femenina de 12 años y más desocupada. | INTEGER |
| PDESOCUP_M | Población masculina de 12 años y más desocupada. | INTEGER |
| PSINDER | Población sin afiliación a servicios de salud. | INTEGER |
| PDER_SS | Población afiliada a servicios de salud. | INTEGER |
| PDER_IMSS | Población afiliada a servicios de salud en el IMSS. | INTEGER |
| PDER_ISTE | Población afiliada a servicios de salud en el ISSSTE. | INTEGER |
| PDER_ISTEE | Población afiliada a servicios de salud en el ISSSTE estatal. | INTEGER |
| PAFIL_PDOM | Población afiliada a servicios de salud en PEMEX, Defensa o Marina. | INTEGER |
| PDER_SEGP | Población afiliada a servicios de salud en el Instituto de Salud para el Bienestar. | INTEGER |
| PDER_IMSSB | Población afiliada a servicios de salud en el IMSS BIENESTAR. | INTEGER |
| PAFIL_IPRIV | Población afiliada a servicios de salud en una institución privada. | INTEGER |
| PAFIL_OTRAI | Población afiliada a servicios de salud en otra institución. | INTEGER |
| P12YM_SOLT | Población de 12 años y más soltera o nunca unida. | INTEGER |
| P12YM_CASA | Población de 12 años y más casada o unida. | INTEGER |
| P12YM_SEPA | Población de 12 años y más que estuvo casada o unida. | INTEGER |
| PCATOLICA | Población con religión católica. | INTEGER |
| PRO_CRIEVA | Población con grupo religioso protestante/cristiano evangélico. | INTEGER |
| POTRAS_REL | Población con otras religiones diferentes a las anteriores. | INTEGER |
| PSIN_RELIG | Población sin religión o sin adscripción religiosa. | INTEGER |
| TOTHOG | Total de hogares censales. | INTEGER |
| HOGJEF_F | Hogares censales con persona de referencia mujer. | INTEGER |
| HOGJEF_M | Hogares censales con persona de referencia hombre. | INTEGER |
| POBHOG | Población en hogares censales. | INTEGER |
| PHOGJEF_F | Población en hogares censales con persona de referencia mujer. | INTEGER |
| PHOGJEF_M | Población en hogares censales con persona de referencia hombre. | INTEGER |
| VIVTOT | Total de viviendas. | BIGINT |
| TVIVHAB | Total de viviendas habitadas. | INTEGER |
| TVIVPAR | Total de viviendas particulares. | INTEGER |
| VIVPAR_HAB | Viviendas particulares habitadas. | INTEGER |
| VIVPARH_CV | Total de viviendas particulares habitadas con características. | INTEGER |
| TVIVPARHAB | Total de viviendas particulares habitadas. | INTEGER |
| VIVPAR_DES | Viviendas particulares deshabitadas. | INTEGER |
| VIVPAR_UT | Viviendas particulares de uso temporal. | INTEGER |
| OCUPVIVPAR | Ocupantes en viviendas particulares habitadas. | INTEGER |
| PROM_OCUP | Promedio de ocupantes en viviendas particulares habitadas. | INTEGER |
| PRO_OCUP_C | Promedio de ocupantes por cuarto en viviendas particulares habitadas. | INTEGER |
| VPH_PISODT | Viviendas particulares habitadas con piso de material diferente de tierra. | INTEGER |
| VPH_PISOTI | Viviendas particulares habitadas con piso de tierra. | INTEGER |
| VPH_1DOR | Viviendas particulares habitadas con un dormitorio. | INTEGER |
| VPH_2YMASD | Viviendas particulares habitadas con dos dormitorios y más. | INTEGER |
| VPH_1CUART | Viviendas particulares habitadas con sólo un cuarto. | INTEGER |
| VPH_2CUART | Viviendas particulares habitadas con dos cuartos. | INTEGER |
| VPH_3YMASC | Viviendas particulares habitadas con 3 cuartos y más. | INTEGER |
| VPH_C_ELEC | Viviendas particulares habitadas que disponen de energía eléctrica. | INTEGER |
| VPH_S_ELEC | Viviendas particulares habitadas que no disponen de energía eléctrica. | INTEGER |
| VPH_AGUADV | Viviendas particulares habitadas que disponen de agua entubada en el ámbito de la vivienda. | INTEGER |
| VPH_AEASP | Viviendas particulares habitadas que disponen de agua entubada y se abastecen del servicio público de agua. | INTEGER |
| VPH_AGUAFV | Viviendas particulares habitadas que no disponen de agua entubada en el ámbito de la vivienda. | INTEGER |
| VPH_TINACO | Viviendas particulares habitadas que disponen de tinaco. | INTEGER |
| VPH_CISTER | Viviendas particulares habitadas que disponen de cisterna o aljibe. | INTEGER |
| VPH_EXCSA | Viviendas particulares habitadas que disponen de excusado o sanitario. | INTEGER |
| VPH_LETR | Viviendas particulares habitadas que disponen de letrina (pozo u hoyo). | INTEGER |
| VPH_DRENAJ | Viviendas particulares habitadas que disponen de drenaje. | INTEGER |
| VPH_NODREN | Viviendas particulares habitadas que no disponen de drenaje. | INTEGER |
| VPH_C_SERV | Viviendas particulares habitadas que disponen de energía eléctrica, agua entubada de la red pública y drenaje. | INTEGER |
| VPH_NDEAED | Viviendas particulares habitadas que no disponen de energía eléctrica, agua entubada, ni drenaje. | INTEGER |
| VPH_DSADMA | Viviendas particulares que disponen de drenaje y sanitario con admisión de agua. | INTEGER |
| VPH_NDACMM | Viviendas particulares habitadas que no disponen de automóvil o camioneta, ni de motocicleta o motoneta. | INTEGER |
| VPH_SNBIEN | Viviendas particulares habitadas sin ningún bien. | INTEGER |
| VPH_REFRI | Viviendas particulares habitadas que disponen de refrigerador. | INTEGER |
| VPH_LAVAD | Viviendas particulares habitadas que disponen de lavadora. | INTEGER |
| VPH_HMICRO | Viviendas particulares habitadas que disponen de horno de microondas. | INTEGER |
| VPH_AUTOM | Viviendas particulares habitadas que disponen de automóvil o camioneta. | INTEGER |
| VPH_MOTO | Viviendas particulares habitadas que disponen de motocicleta o motoneta. | INTEGER |
| VPH_BICI | Viviendas particulares habitadas que disponen de bicicleta como medio de transporte. | INTEGER |
| VPH_RADIO | Viviendas particulares habitadas que disponen de radio. | INTEGER |
| VPH_TV | Viviendas particulares habitadas que disponen de televisor. | INTEGER |
| VPH_PC | Viviendas particulares habitadas que disponen de computadora, laptop o tablet. | INTEGER |
| VPH_TELEF | Viviendas particulares habitadas que disponen de línea telefónica fija. | INTEGER |
| VPH_CEL | Viviendas particulares habitadas que disponen de teléfono celular. | INTEGER |
| VPH_INTER | Viviendas particulares habitadas que disponen de Internet. | INTEGER |
| VPH_STVP | Viviendas particulares habitadas que disponen de servicio de televisión de paga. | INTEGER |
| VPH_SPMVPI | Viviendas particulares habitadas que disponen de servicio de películas, música o videos de paga por Internet. | INTEGER |
| VPH_CVJ | Viviendas particulares habitadas que disponen de consola de videojuegos. | INTEGER |
| VPH_SINRTV | Viviendas particulares habitadas sin radio ni televisor. | INTEGER |
| VPH_SINLTC | Viviendas particulares habitadas sin línea telefónica fija ni teléfono celular. | INTEGER |
| VPH_SINCINT | Viviendas particulares habitadas sin computadora ni Internet. | INTEGER |
| VPH_SINTIC | Viviendas particulares habitadas sin tecnologías de la información y de la comunicación (TIC). | INTEGER |

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
