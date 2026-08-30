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


def escribir_bytes_archivo(ruta: str, contenido: bytes) -> None:
    """
    Escribe un bloque de bytes en un archivo

    Params:
        ruta (str): Ruta del archivo destino
        contenido (bytes): Bytes a escribir
    """
    directorio = os.path.dirname(ruta)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)

    with open(ruta, "wb") as archivo:
        archivo.write(contenido)


def guardar_descifrado(descifrado: bytes, nombre: str, extension: str) -> str:
    """
    Guarda el resultado de un descifrado en un archivo

    Params:
        descifrado (bytes): Contenido descifrado a guardar
        nombre (str): Nombre base del archivo
        extension (str): Extensión del archivo

    Returns:
        str: Ruta completa del archivo guardado.
    """
    ruta = f"{nombre}_descifrado.{extension}"
    escribir_bytes_archivo(ruta, descifrado)
    return ruta