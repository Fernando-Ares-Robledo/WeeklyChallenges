"""
TASK #1: Self Spammer

Write a program which outputs one word of its own script / source code at random. A word is anything between whitespace, including symbols.

Basic level
"""

import random

with open(__file__, 'r') as archivo:
    lineas = archivo.readlines()
lineas = [linea for linea in lineas if linea.strip()]

linea_aleatoria = random.choice(lineas)
palabra = random.choice(linea_aleatoria.split())
print(palabra)