##
def base64_encode(data: bytes) -> str:
    CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    completo= len(data)%3
    p= 0 if completo == 0 else(3 - completo)
    while len(data)%6 !=0:
        data +="0"
    res=""
    for i in range(0,len(data),6):
        bloque = data[i:i+6]
        indi=int(bloque,2)
        res+= CARACTERES[indi]
    if p>0:
        res=res[:-p]+("="*p)
    return res
def base64_decode(encoded: str) -> bytes:
    word = encoded.replace("=", "")
    CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    res = ""
    for char in word:
        if char in CARACTERES:
            index = CARACTERES.index(char)
            res += format(index, '06b')
    while len(res) % 8 != 0:
        res = res[:-1]

    result = b""
    for i in range(0, len(res), 8):
        byte = res[i:i+8]
        if len(byte) == 8:
            result += bytes([int(byte, 2)])
    return result
