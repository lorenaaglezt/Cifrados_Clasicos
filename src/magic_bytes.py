MAGIC_BYTES_HEX = {
    "89504e470d0a1a0a": "png",
    "ffd8ff": "jpg",
    "424d": "bmp",
    "494433": "mp3",
    "fffb": "mp3",
    "4f676753": "ogg",            # OggS
    "0000001866747970": "mp4",
    "1a45dfa3": "mkv",
    "504b0304": "docx",           # PK.. (También zip, epub, xlsx...)
    "25504446": "pdf",            # %PDF
    "65707562": "epub",           # epub
}

RIFF = "52494646"

def detectar_formato(data: bytes) -> str | None:
    """
    Determina el formato de un archivo a partir de su contenido binario.

    Params:
        data: Contenido binario del archivo

    Returns:
        Formato del archivo como string o None si no se puede determinar.
    """
    if hasattr(data, 'read'):
        start_pos = data.tell() if hasattr(data, 'tell') else 0
        bytes_data = data.read(16)
        if hasattr(data, 'seek'):
            data.seek(start_pos)
    else:
        bytes_data = data[:16]

    hexbytes = bytes_data.hex()

    # Para el caso de RIFF, WAV y AVI comparten los primeros 4 bytes.
    # Los bytes 8-11 indican el subtipo sea wav o avi
    if hexbytes.startswith(RIFF) and len(bytes_data) >= 12:
        subtype = bytes_data[8:12]
        if subtype == b"WAVE":
            return "wav"
        if subtype == b"AVI ":
            return "avi"
        return None  # tipo desconocido

    for magic_hex, formato in MAGIC_BYTES_HEX.items():
        if hexbytes.startswith(magic_hex):
            return formato

    return None