import sys
import math
from pathlib import Path

from archivos_bytes import leer_archivo
from magic_bytes import detectar_formato
from base64_codec import base64_decode

from ciphers import (
    cesar_descifrar,
    decimado_descifrar,
    afin_descifrar,
)

DIRECTORIO_SALIDA = Path("archivos_descifrados")

# Llaves validas para Decimado
LLAVES_DECIMADO = [a for a in range(1, 256) if math.gcd(a, 256) == 1]


# FUNCIONES AUXILIARES

def guardar(datos: bytes, nombre_base: str, formato: str) -> Path | None:
    """Crea el directorio de salida si no existe y guarda el archivo.

    Returns:
        Path al archivo guardado, o None si no se pudo escribir.
    """
    DIRECTORIO_SALIDA.mkdir(exist_ok=True)
    ruta = DIRECTORIO_SALIDA / f"{nombre_base}_descifrado.{formato}"
    try:
        ruta.write_bytes(datos)
    except (PermissionError, OSError) as e:
        print(f"Error al escribir: {e}")
        return None
    return ruta



def resultado(cifrado: str, llave: str, formato: str, ruta: Path) -> None:
    """Imprime el resultado del descifrado.
    
    Args:
        cifrado: Tipo de cifrado
        llave: Llave utilizada
        formato: Formato del archivo descifrado
        ruta: Ruta del archivo descifrado
    """
    print(f"Cifrado : {cifrado}")
    print(f"Llave : {llave}")
    print(f"Formato : {formato}")
    print(f"Ruta : {ruta}")


# FUERZA BRUTA EN LOS CIFRADOS

def base64_fuerza_bruta(datos: bytes, nombre_archivo: str) -> bool:
    """
    Intenta interpretar los datos como un archivo codificado en Base64.

    Params:
        datos (bytes): Bytes del archivo a descifrar
        nombre_archivo (str): Nombre del archivo sin extensión

    Returns:
        bool: True si se encontro y guardo el archivo, False en caso contrario.
    """
    print("\nINTENTO Base64\n")
    try:
        # Los datos pueden venir como bytes o como texto Base64
        texto = datos.decode("ascii", errors="ignore").strip()
        descifrado = base64_decode(texto)
        
        if len(descifrado) >= 16:
            formato = detectar_formato(descifrado)
            if formato:
                ruta = guardar(descifrado, nombre_archivo, formato)
                if ruta:
                    resultado("Base64", "NA", formato, ruta)
                    return True
    except Exception:
        pass

    print("Base64: sin resultado.")
    return False


def cesar_fuerza_bruta(datos: bytes, nombre_archivo: str) -> bool:
    """
    Fuerza bruta sobre las 256 llaves del cifrado Cesar.

    Params:
        datos (bytes): Bytes del archivo a descifrar
        nombre_archivo (str): Nombre del archivo sin extensión

    Returns:
        bool: True si se encontro y guardo el archivo, False en caso contrario.
    """
    print("\nINTENTO Cesar\n")

    cabecera = datos[:16]

    # Aplicamos para las 256 llaves
    for k in range(256):
        descifrado_cabecera = cesar_descifrar(cabecera, k)
        formato = detectar_formato(descifrado_cabecera)
        if formato:
            # Si el formato es valido, desciframos el archivo completo
            descifrado_completo = cesar_descifrar(datos, k)
            ruta = guardar(descifrado_completo, nombre_archivo, formato)
            if ruta:
                resultado("Cesar", str(k), formato, ruta)
                return True

    print("Cesar: sin resultado.")
    return False


def decimado_fuerza_bruta(datos: bytes, nombre_archivo: str) -> bool:
    """
    Fuerza bruta sobre las llaves validas del cifrado Decimado
    (valores coprimos con 256).

    Params:
        datos (bytes): Bytes del archivo a descifrar
        nombre_archivo (str): Nombre del archivo sin extensión

    Returns:
        bool: True si se encontro y guardo el archivo, False en caso contrario.
    """
    print("\nINTENTO Decimado\n")

    cabecera = datos[:16]

    for a in LLAVES_DECIMADO:
        descifrado_cabecera = decimado_descifrar(cabecera, a)
        formato = detectar_formato(descifrado_cabecera)
        if formato:
            descifrado_completo = decimado_descifrar(datos, a)
            ruta = guardar(descifrado_completo, nombre_archivo, formato)
            if ruta:
                resultado("Decimado", str(a), formato, ruta)
                return True

    print("Decimado: sin resultado.")
    return False


def afin_fuerza_bruta(datos: bytes, nombre_archivo: str) -> bool:
    """
    Fuerza bruta sobre todas las combinaciones (a, c) del cifrado Afin con a coprimo con 256 (128 valores)
    y c en 0-255 (256 valores)

    Params:
        datos (bytes): Bytes del archivo a descifrar
        nombre_archivo (str): Nombre del archivo sin extensión

    Returns:
        bool: True si se encontro y guardo el archivo, False en caso contrario.
    """
    print("\nINTENTO Afin\n")
    
    combinaciones = len(LLAVES_DECIMADO) * 256
    cabecera = datos[:16]

    for a in LLAVES_DECIMADO:
        for c in range(256):
            descifrado_cabecera = afin_descifrar(cabecera, a, c)
            formato = detectar_formato(descifrado_cabecera)
            if formato:
                descifrado_completo = afin_descifrar(datos, a, c)
                ruta = guardar(descifrado_completo, nombre_archivo, formato)
                if ruta:
                    resultado("Afin", f"a={a}, c={c}", formato, ruta)
                    return True

    print("Afin: sin resultado.")
    return False



# DESCIFRADOR

METODOS_CIFRADO = [
    base64_fuerza_bruta,
    cesar_fuerza_bruta,
    decimado_fuerza_bruta,
    afin_fuerza_bruta,
]

def descifrar_archivo(ruta_cifrado: str) -> None:
    """
    Prueba cada estrategia de descifrado en orden hasta encontrar una que funcione.

    Params:
        ruta_cifrado (str): Ruta al archivo cifrado
    """
    ruta = Path(ruta_cifrado)

    if not ruta.is_file():
        print(f"No se encontro el archivo")
        sys.exit(1)

    nombre_base = ruta.stem  # nombre sin extension

    print(f"\nArchivo : {ruta}\n")

    datos = leer_archivo(str(ruta))

    for metodo in METODOS_CIFRADO:
        if metodo(datos, nombre_base):
            break


def main() -> None:
    if len(sys.argv) < 2:
        print("Necesitas indicar la ruta del archivo a cifrar.")
        sys.exit(1)

    ruta_cifrado = sys.argv[1]
    descifrar_archivo(ruta_cifrado)


if __name__ == "__main__":
    main()
