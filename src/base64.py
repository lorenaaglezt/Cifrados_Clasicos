def base64_encode(data: bytes) -> str:
    """
    Codifica una secuencia de bytes a Base64.

    Args:
        data: Bytes a codificar

    Returns:
        Cadena codificada en Base64
    """
    CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    completo = len(data) % 3
    p = 0 if completo == 0 else (3 - completo)
    data_padded = data + b"\x00" * p
    bits = "".join(format(b, "08b") for b in data_padded)
    res = "".join(CARACTERES[int(bits[i:i+6], 2)] for i in range(0, len(bits), 6))
    if p > 0:
        res = res[:-p] + ("=" * p)
    return res


def base64_decode(encoded: str) -> bytes:
    """
    Decodifica una secuencia de Base64 a bytes.

    Args:
        encoded: Cadena codificada en Base64

    Returns:
        Bytes decodificados
    """
    CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    BUSQUEDA = {c: i for i, c in enumerate(CARACTERES)}

    padding = encoded.count("=")
    word = encoded.replace("=", "")
    vals = [BUSQUEDA[c] for c in word if c in BUSQUEDA]
    while len(vals) % 4 != 0:
        vals.append(0)

    result = bytearray()
    for i in range(0, len(vals), 4):
        n = (vals[i] << 18) | (vals[i+1] << 12) | (vals[i+2] << 6) | vals[i+3]
        result.append((n >> 16) & 0xFF)
        result.append((n >> 8) & 0xFF)
        result.append(n & 0xFF)

    if padding:
        del result[-padding:]

    return bytes(result)