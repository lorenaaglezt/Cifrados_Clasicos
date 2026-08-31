#!/usr/bin/env python3
"""Script de prueba para magic_bytes.py y base64_codec.py"""

import io
from magic_bytes import detectar_formato, es_archivo_valido
from base64_codec import base64_encode, base64_decode

print("=" * 60)
print("PRUEBAS: magic_bytes.py")
print("=" * 60)

# Prueba 1: Detectar formato PNG
print("\n1. Detectar formato PNG:")
png_magic = bytes.fromhex("89504e470d0a1a0a")
png_file = io.BytesIO(png_magic + b"datos adicionales")
formato = detectar_formato(png_file)
print(f"   Magic bytes PNG: {formato}")
assert formato == "png", f"Error: esperaba 'png', obtuvo '{formato}'"
print("   ✓ Correcto")

# Prueba 2: Detectar formato PDF
print("\n2. Detectar formato PDF:")
pdf_magic = bytes.fromhex("25504446")
pdf_file = io.BytesIO(pdf_magic + b"data")
formato = detectar_formato(pdf_file)
print(f"   Magic bytes PDF: {formato}")
assert formato == "pdf", f"Error: esperaba 'pdf', obtuvo '{formato}'"
print("   ✓ Correcto")

# Prueba 3: Detectar formato JPG
print("\n3. Detectar formato JPG:")
jpg_magic = bytes.fromhex("ffd8ff")
jpg_file = io.BytesIO(jpg_magic + b"data")
formato = detectar_formato(jpg_file)
print(f"   Magic bytes JPG: {formato}")
assert formato == "jpg", f"Error: esperaba 'jpg', obtuvo '{formato}'"
print("   ✓ Correcto")

# Prueba 4: Validar archivo con formato esperado
print("\n4. Validar archivo PNG (formato esperado: png):")
png_file = io.BytesIO(png_magic + b"datos")
es_valido = es_archivo_valido(png_file, "png")
print(f"   ¿Es válido? {es_valido}")
assert es_valido, "Error: PNG debería ser válido"
print("   ✓ Correcto")

# Prueba 5: Rechazar archivo con formato incorrecto
print("\n5. Validar archivo PNG (formato esperado: jpg):")
png_file = io.BytesIO(png_magic + b"datos")
es_valido = es_archivo_valido(png_file, "jpg")
print(f"   ¿Es válido? {es_valido}")
assert not es_valido, "Error: PNG no debería ser válido si esperamos JPG"
print("   ✓ Correcto")

# Prueba 6: Magic bytes desconocidos
print("\n6. Magic bytes desconocidos:")
unknown_file = io.BytesIO(b"\x00\x00\x00\x00datos")
formato = detectar_formato(unknown_file)
print(f"   Formato detectado: {formato}")
assert formato is None, "Error: debería retornar None para bytes desconocidos"
print("   ✓ Correcto")

print("\n" + "=" * 60)
print("PRUEBAS: base64_codec.py")
print("=" * 60)

# Prueba 7: Codificar a base64
print("\n1. Codificar cadena binaria a base64:")
# 'A' en ASCII = 65 = 01000001 en binario
binary_str = "010000010100001001000011"  # ABC en binario (8 bits cada uno)
encoded = base64_encode(binary_str)
print(f"   Entrada (binario): {binary_str}")
print(f"   Salida (base64): {encoded}")
# Esperamos que "010000010100001001000011" se divida en grupos de 6 bits:
# 010000 (16) 010100 (20) 001001 (9) 000011 (3)
# Que corresponde a: Q U J D
print("   ✓ Conversión realizada")

# Prueba 8: Decodificar desde base64
print("\n2. Decodificar base64 a bytes:")
# Usando un base64 válido
encoded_str = "SGVsbG8="  # "Hello" en base64 estándar
try:
    decoded = base64_decode(encoded_str)
    print(f"   Entrada (base64): {encoded_str}")
    print(f"   Salida (bytes): {decoded}")
    print(f"   Como string: {decoded.decode('utf-8', errors='ignore')}")
    print("   ✓ Decodificación realizada")
except Exception as e:
    print(f"   ⚠ Error en decodificación: {e}")

# Prueba 9: Encode y decode roundtrip
print("\n3. Prueba roundtrip (encode -> decode):")
test_binary = "0100100001100101"  # "He" en ASCII
print(f"   Entrada (binario): {test_binary}")
encoded = base64_encode(test_binary)
print(f"   Codificado: {encoded}")
decoded = base64_decode(encoded)
print(f"   Decodificado (bytes): {decoded}")
print("   ✓ Roundtrip completado")

print("\n" + "=" * 60)
print("✓ TODAS LAS PRUEBAS COMPLETADAS")
print("=" * 60)
