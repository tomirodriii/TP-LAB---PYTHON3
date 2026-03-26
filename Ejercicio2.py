## Funciones:
#   2. Definir función, parámetros, retorno, capturar un valor o varios

import os
os.system("cls")

def saludar(nombre):
    return f"Hola, {nombre}!, ¿Como te encuentras?"
usuario = input("Ingrese su nombre: ")
mensaje_saludo = saludar(usuario)
print(mensaje_saludo)

