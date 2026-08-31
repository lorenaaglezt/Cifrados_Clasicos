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
    if hasattr(data, 'read'):
        start_pos = data.tell() if hasattr(data, 'tell') else 0
        bytes_data = data.read(16)
        if hasattr(data, 'seek'):
            data.seek(start_pos)
    else:
        bytes_data = data[:16]
    
    hexbytes = bytes_data.hex()
    
    
    for magic_hex, formato in MAGIC_BYTES_HEX.items():
        if hexbytes.startswith(magic_hex):
            return formato
    
    return None
def es_archivo_valido(data: bytes, formato_esperado: str) -> bool:
    formato_detectado = detectar_formato(data)
    return formato_detectado == formato_esperado