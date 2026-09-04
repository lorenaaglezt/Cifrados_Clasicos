"""
Funciones para leer y escribir archivos a nivel de bytes.
"""

import os

def leer_archivo(ruta: str) -> bytes:
    """
    Lee el contenido completo de un archivo y lo devuelve como bytes

    Params:
        ruta (str): Ruta al archivo que se quiere leer

    Returns:
        bytes: Contenido completo del archivo
    """
    if not os.path.isfile(ruta):
        raise FileNotFoundError(f"No se encontró el archivo")

    with open(ruta, "rb") as archivo:
        return archivo.read()