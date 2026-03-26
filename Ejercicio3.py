# Funciones:
#   3. Contar palabras

import os
os.system("cls")

def contar_palabras(frase):
    
    palabras = frase.split()
    return len(palabras)
frase= input("Ingrese una frase: ")
cantidad_palabras = contar_palabras(frase)
print(f"La frase ingresada tiene {cantidad_palabras} palabras.")

