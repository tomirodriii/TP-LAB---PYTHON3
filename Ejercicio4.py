# Funciones:
# 4. Verificación de Palíndromos

import os
os.system("cls")

def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]