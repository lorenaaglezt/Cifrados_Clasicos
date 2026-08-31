MAGIC_BYTES_HEX = {
    "89504e470d0a1a0a": "png",
    "ffd8ff": "jpg",
    "424d": "bmp",
    "494433": "mp3",
    "fffb": "mp3",
    "52494646": "wav",  # RIFF (Requiere 'WAVE' en bytes 8-11)
    "4f676753": "ogg",   # OggS
    "0000001866747970": "mp4",
    "52494646": "avi",  # RIFF (Requiere 'AVI ' en bytes 8-11)
    "1a45dfa3": "mkv",
    "504b0304": "docx", # PK.. (También zip, epub, xlsx...)
    "25504446": "pdf",  # %PDF
    "65707562": "epub", # epub
}

def detectar_formato(data: bytes) -> str | None:
    primer= data.read(4)
    hexbytes= primer.hex()
    res= MAGIC_BYTES_HEX.get(hexbytes)
    return res
def es_archivo_valido(data: bytes, formato_esperado: str) -> bool:
    formato_detectado = detectar_formato(data)
    return formato_detectado == formato_esperado