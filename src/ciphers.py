"""
Funciones para cifrar y descifrar datos
"""

def cesar_cifrar(data: bytes, k: int) -> bytes:
    """
    Cifra los bytes utilizando el cifrado Cesar
    Cada byte se desplaza k posiciones y la operación con módulo 256.
    Params:
        data (bytes): Lo que se quiere descifrar
        k (int): Llave o la cantidad de posiciones que se desplazarán los bytes.
    Returns:
         bytes: Contenido cifrado.
    """
    resultado = bytes((byte + k) % 256 for byte in data)
    return resultado

def cesar_descifrar(data: bytes, k: int) -> bytes:
    """
    Descifra los bytes usando el cifrado César
    Cada bye se desplaza k posiciones en sentido contrario y la operación con módulo 256
    Params:
        data (bytes): el cifrado que se quiere descifrar.
        k (int): Llave usada en el cifrado.
    Returns:
        bytes: Contenido cifrado.
    """
    resultado = bytes((byte - k) % 256 for byte in data)
    return resultado

"""
PRUEBA:
data = bytes([10, 20, 30])
cifrado = cesar_cifrar(data, 5)
print("Cifrado: ", cifrado)
descifrado = cesar_descifrar(cifrado, 5)
print ("Descifrado: ", descifrado)
assert descifrado == data
print("Si funciona")
"""

def inverso_modular(a: int, m:int) -> int:
    """
    Calcula el inverso modular de un número usando el algoritmo de Euclides.
    El inverso modular x es:
        (a * x) mod m = 1
    Params:
        a (int): Número de, que se quiere sacar el inverso.
        m (int): Módulo usado para calcular el inverso.
    Return:
        int: Inverso modular de a módulo m.
    Raises:
        ValueError: Si el inverso modular no existe.
    """
    m_original = m
    x0 = 1
    x1 = 0
    while m != 0:
        cociente = a // m
        a, m = m, a % m
        x0, x1 = x1, x0 - cociente * x1
    if a != 1:
        raise ValueError("Si no existe el inverso modular")
    return x0 % m_original

"""PRUEBA:
print("Inverso de 3:", inverso_modular(3, 256))
assert inverso_modular(3, 256) == 171
print("Si funciona")
"""

