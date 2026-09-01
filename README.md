# Cifrados Clásicos

- Aguirre Cruz Cassandra
- González Téllez Lorena
- Vázquez Rincón Oscar

## Descripción

Esta práctica tiene como objetivo implementar algunos cifrados clásicos y aplicarlos para el cifrado y el
descifrado de archivos. El desarrollo de la misma implica trabajar directamente a nivel de bytes y realizar corrimientos correspondientes según el cifrado empleado. El enfoque se centra en el cifrado César, el cifrado
decimado, el cifrado afín y la codificación Base64. Para poder descifrar los archivos sin conocer
la llave de antemano, se hace uso de las firmas de archivo o Magic Bytes. Se busca combinar este conocimiento con las propiedades 
matemáticas de los cifrados para deducir la llave correcta y recuperar los archivos originales.

La importancia de esta práctica radica en comprender la base y los cimientos de lo que es la
criptografía moderna. Saber aplicar estos cifrados clásicos permite construir bases sólidas sobre el origen de la disciplina,
aplicando congruencias y aritmética modular. Por otro lado, el enfrentarse a un escenario de descifrado, como el que plantea 
esta práctica, nos permite desarrollar conocimientos sobre el manejo de bytes y las firmas de archivo.

## Requisitos

- Python 3.10 o superior.
- No se requieren librerías externas. Todo el código utiliza la biblioteca estándar de Python.

## Cómo correr y usar el programa

La herramienta se ejecuta desde la línea de comandos. El script principal es `main.py`, ubicado dentro del directorio `src`.

### Uso

Después de clonar el repositorio situarse en el directorio raíz. Para intentar descifrar un archivo, debes pasar la ruta del archivo cifrado como argumento al script `main.py`:

```bash
python src/main.py <ruta del archivo cifrado>
```