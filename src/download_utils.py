import os
import requests
import time
from zipfile import ZipFile
from tqdm import tqdm

def download_file(url, directory):
    """Descarga un archivo desde una URL a un directorio, con barra de progreso.

    Args:
        url (str): La URL del archivo a descargar.
        directory (str): El directorio donde se guardará el archivo.

    Returns:
        str: La ruta completa al archivo descargado, o None si falla.
    """
    os.makedirs(directory, exist_ok=True)
    filename = url.split('/')[-1]
    filepath = os.path.join(directory, filename)

    if os.path.exists(filepath):
        print(f"INFO: El archivo {filename} ya existe en {directory}. No se descargará de nuevo.")
        return filepath

    try:
        print(f"Descargando {filename}...")
        time.sleep(1)  # Pequeña pausa para no saturar el servidor
        r = requests.get(url, stream=True, timeout=300) # Timeout de 5 minutos
        r.raise_for_status()  # Lanza una excepción para códigos de error HTTP

        total_size = int(r.headers.get('content-length', 0))

        with open(filepath, 'wb') as f, tqdm(
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            desc=filename
        ) as pbar:
            for data in r.iter_content(chunk_size=1024):
                size = f.write(data)
                pbar.update(size)

        print(f"Descarga completada: {filepath}")
        return filepath

    except requests.exceptions.RequestException as e:
        print(f"ERROR: No se pudo descargar {url}. Razón: {e}")
        if os.path.exists(filepath):
            os.remove(filepath) # Eliminar archivo parcial si existe
        return None

def extract_zip(zip_path, extract_to_dir, specific_files=None):
    """Extrae todos los archivos o archivos específicos de un ZIP.

    Args:
        zip_path (str): La ruta al archivo ZIP.
        extract_to_dir (str): El directorio donde se extraerán los archivos.
        specific_files (list, optional): Lista de archivos específicos a extraer del ZIP. 
                                         Si es None, extrae todo. Defaults to None.
    """
    os.makedirs(extract_to_dir, exist_ok=True)
    try:
        with ZipFile(zip_path, 'r') as zip_ref:
            if specific_files:
                for file_path in specific_files:
                    # Comprobar si el archivo existe en el ZIP antes de extraer
                    if file_path in zip_ref.namelist():
                        zip_ref.extract(file_path, extract_to_dir)
                    else:
                        print(f"ADVERTENCIA: El archivo {file_path} no se encontró en {zip_path}")
            else:
                zip_ref.extractall(extract_to_dir)
        #print(f"Archivos extraídos de {os.path.basename(zip_path)} a {extract_to_dir}")

    except FileNotFoundError:
        print(f"ERROR: El archivo ZIP no se encontró en {zip_path}")
    except Exception as e:
        print(f"ERROR: Ocurrió un error al extraer {zip_path}: {e}")
