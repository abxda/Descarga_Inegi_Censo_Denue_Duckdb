import os

# 1. Configuración General
# --------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DB_PATH = os.path.join(BASE_DIR, 'output', 'censo_denue.duckdb')

# 2. Listas de Estados
# --------------------------------------------------
# Nombres de los archivos ZIP del Marco Geoestadístico
ESTADOS_GEO = [
    "01_aguascalientes.zip", "02_bajacalifornia.zip", "03_bajacaliforniasur.zip",
    "04_campeche.zip", "05_coahuiladezaragoza.zip", "06_colima.zip", "07_chiapas.zip",
    "08_chihuahua.zip", "09_ciudaddemexico.zip", "10_durango.zip", "11_guanajuato.zip",
    "12_guerrero.zip", "13_hidalgo.zip", "14_jalisco.zip", "15_mexico.zip",
    "16_michoacandeocampo.zip", "17_morelos.zip", "18_nayarit.zip", "19_nuevoleon.zip",
    "20_oaxaca.zip", "21_puebla.zip", "22_queretaro.zip", "23_quintanaroo.zip",
    "24_sanluispotosi.zip", "25_sinaloa.zip", "26_sonora.zip", "27_tabasco.zip",
    "28_tamaulipas.zip", "29_tlaxcala.zip", "30_veracruzignaciodelallave.zip",
    "31_yucatan.zip", "32_zacatecas.zip"
]

# Números correspondientes a cada estado
ESTADOS_NUM = list(range(1, 33))

# URLs para la descarga de datos del DENUE
URLS_DENUE = [
    f"https://www.inegi.org.mx/contenidos/masiva/denue/denue_{str(i).zfill(2)}_shp.zip"
    for i in list(range(1, 15)) + ["15_1", "15_2"] + list(range(16, 33))
]

# 3. URLs Base de INEGI
# --------------------------------------------------
BASE_URL_CENSO_CSV = "https://www.inegi.org.mx/contenidos/programas/ccpv/2020/datosabiertos/ageb_manzana/"
BASE_URL_MARCO_GEO = "https://www.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/geografia/marcogeo/889463807469/"

# 4. Rutas de Directorios
# --------------------------------------------------
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Directorios para Censo y Marco Geoestadístico
CENSO_DIR = os.path.join(DATA_DIR, 'censo')
CENSO_RAW_ZIP_DIR = os.path.join(CENSO_DIR, 'raw_zip')
CENSO_CSV_DIR = os.path.join(CENSO_DIR, 'csv')
CENSO_PARQUET_DIR = os.path.join(CENSO_DIR, 'parquet')

MARCO_GEO_DIR = os.path.join(DATA_DIR, 'mg_marco_geo')
MARCO_GEO_RAW_ZIP_DIR = os.path.join(MARCO_GEO_DIR, 'raw_zip')
MARCO_GEO_SHP_DIR = os.path.join(MARCO_GEO_DIR, 'shp')
MARCO_GEO_GEOPARQUET_DIR = os.path.join(MARCO_GEO_DIR, 'geoparquet')

# Directorios para DENUE
DENUE_DIR = os.path.join(DATA_DIR, 'denue')
DENUE_RAW_ZIP_DIR = os.path.join(DENUE_DIR, 'raw_zip')
DENUE_SHP_DIR = os.path.join(DENUE_DIR, 'shp')
DENUE_GEOPARQUET_DIR = os.path.join(DENUE_DIR, 'geoparquet')

# 5. Parámetros de Procesamiento
# --------------------------------------------------
# Proyección de origen para los datos del Marco Geoestadístico
CRS_ORIGEN = "EPSG:6372"
# Proyección de destino para todos los datos geoespaciales
CRS_DESTINO = "EPSG:4326"

# Valores a tratar como nulos en los datos del censo
CENSO_NULL_VALUES = {'N/A': None, 'N/D': None, '*': None, '': None}

# Lista de columnas del censo que deben ser convertidas a tipo INTEGER
CENSO_COLUMNAS_A_INT = [
    "POBFEM", "POBMAS", "P_0A2", "P_0A2_F", "P_0A2_M", "P_3YMAS", "P_3YMAS_F", "P_3YMAS_M",
    "P_5YMAS", "P_5YMAS_F", "P_5YMAS_M", "P_12YMAS", "P_12YMAS_F", "P_12YMAS_M", "P_15YMAS", "P_15YMAS_F",
    "P_15YMAS_M", "P_18YMAS", "P_18YMAS_F", "P_18YMAS_M", "P_3A5", "P_3A5_F", "P_3A5_M", "P_6A11",
    "P_6A11_F", "P_6A11_M", "P_8A14", "P_8A14_F", "P_8A14_M", "P_12A14", "P_12A14_F", "P_12A14_M",
    "P_15A17", "P_15A17_F", "P_15A17_M", "P_18A24", "P_18A24_F", "P_18A24_M", "P_15A49_F", "P_60YMAS",
    "P_60YMAS_F", "P_60YMAS_M", "REL_H_M", "POB0_14", "POB15_64", "POB65_MAS", "PROM_HNV", "PNACENT",
    "PNACENT_F", "PNACENT_M", "PNACOE", "PNACOE_F", "PNACOE_M", "PRES2015", "PRES2015_F", "PRES2015_M",
    "PRESOE15", "PRESOE15_F", "PRESOE15_M", "P3YM_HLI", "P3YM_HLI_F", "P3YM_HLI_M", "P3HLINHE", "P3HLINHE_F",
    "P3HLINHE_M", "P3HLI_HE", "P3HLI_HE_F", "P3HLI_HE_M", "P5_HLI", "P5_HLI_NHE", "P5_HLI_HE", "PHOG_IND",
    "POB_AFRO", "POB_AFRO_F", "POB_AFRO_M", "PCON_DISC", "PCDISC_MOT", "PCDISC_VIS", "PCDISC_LENG",
    "PCDISC_AUD", "PCDISC_MOT2", "PCDISC_MEN", "PCON_LIMI", "PCLIM_CSB", "PCLIM_VIS", "PCLIM_HACO",
    "PCLIM_OAUD", "PCLIM_MOT2", "PCLIM_RE_CO", "PCLIM_PMEN", "PSIND_LIM", "P3A5_NOA", "P3A5_NOA_F",
    "P3A5_NOA_M", "P6A11_NOA", "P6A11_NOAF", "P6A11_NOAM", "P12A14NOA", "P12A14NOAF", "P12A14NOAM",
    "P15A17A", "P15A17A_F", "P15A17A_M", "P18A24A", "P18A24A_F", "P18A24A_M", "P8A14AN", "P8A14AN_F",
    "P8A14AN_M", "P15YM_AN", "P15YM_AN_F", "P15YM_AN_M", "P15YM_SE", "P15YM_SE_F", "P15YM_SE_M",
    "P15PRI_IN", "P15PRI_INF", "P15PRI_INM", "P15PRI_CO", "P15PRI_COF", "P15PRI_COM", "P15SEC_IN",
    "P15SEC_INF", "P15SEC_INM", "P15SEC_CO", "P15SEC_COF", "P15SEC_COM", "P18YM_PB", "P18YM_PB_F",
    "P18YM_PB_M", "GRAPROES", "GRAPROES_F", "GRAPROES_M", "PEA", "PEA_F", "PEA_M", "PE_INAC",
    "PE_INAC_F", "PE_INAC_M", "POCUPADA", "POCUPADA_F", "POCUPADA_M", "PDESOCUP", "PDESOCUP_F",
    "PDESOCUP_M", "PSINDER", "PDER_SS", "PDER_IMSS", "PDER_ISTE", "PDER_ISTEE", "PAFIL_PDOM",
    "PDER_SEGP", "PDER_IMSSB", "PAFIL_IPRIV", "PAFIL_OTRAI", "P12YM_SOLT", "P12YM_CASA", "P12YM_SEPA",
    "PCATOLICA", "PRO_CRIEVA", "POTRAS_REL", "PSIN_RELIG", "TOTHOG", "HOGJEF_F", "HOGJEF_M",
    "POBHOG", "PHOGJEF_F", "PHOGJEF_M", "TVIVHAB", "TVIVPAR", "VIVPAR_HAB", "VIVPARH_CV",
    "TVIVPARHAB", "VIVPAR_DES", "VIVPAR_UT", "OCUPVIVPAR", "PROM_OCUP", "PRO_OCUP_C", "VPH_PISODT",
    "VPH_PISOTI", "VPH_1DOR", "VPH_2YMASD", "VPH_1CUART", "VPH_2CUART", "VPH_3YMASC", "VPH_C_ELEC",
    "VPH_S_ELEC", "VPH_AGUADV", "VPH_AEASP", "VPH_AGUAFV", "VPH_TINACO", "VPH_CISTER", "VPH_EXCSA",
    "VPH_LETR", "VPH_DRENAJ", "VPH_NODREN", "VPH_C_SERV", "VPH_NDEAED", "VPH_DSADMA", "VPH_NDACMM",
    "VPH_SNBIEN", "VPH_REFRI", "VPH_LAVAD", "VPH_HMICRO", "VPH_AUTOM", "VPH_MOTO", "VPH_BICI",
    "VPH_RADIO", "VPH_TV", "VPH_PC", "VPH_TELEF", "VPH_CEL", "VPH_INTER", "VPH_STVP", "VPH_SPMVPI",
    "VPH_CVJ", "VPH_SINRTV", "VPH_SINLTC", "VPH_SINCINT", "VPH_SINTIC"
]
