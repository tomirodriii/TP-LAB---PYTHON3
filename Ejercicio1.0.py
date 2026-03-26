# 1. Define una lista de diccionarios que represente información personal. nombre,edad. Luego, accede a
# elementos específicos de la lista, como el primer diccionario, el nombre de la primera persona y la edad de la 
# segunda persona, para finalmente imprimir los resultados en la consola. 
# 1.2. Del punto 1, recorrer y mostrar k,v

import os
os.system("cls")

listanombres = [
    
    {"Nombre": "Juan", "Edad": 30},
    {"Nombre": "Tomás", "Edad": 17},
    {"Nombre": "Ramiro", "Edad": 20},
    {"Nombre": "María", "Edad": 25},
    {"Nombre": "Pedro", "Edad": 40}
]


primer_persona = listanombres[0]["Nombre"]
edad_segunda_persona = listanombres[1]["Edad"]
print("Nombre de la primera persona:", primer_persona)
print("Edad de la segunda persona:", edad_segunda_persona)

for diccionario in listanombres: # punto 1.2
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
    print()  
    








