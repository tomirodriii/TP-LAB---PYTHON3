# Funciones:
#7. Integrador: Crear programa que permita al usuario agregar tareas con descripción, 
# fecha límite y prioridad, así como mostrar  la lista de tareas. 
# Este menú se repite hasta que el usuario elige salir."

import os
os.system("cls")

lista_tareas = []  

seguir = True
while seguir:
    tarea = input("Ingrese el nombre de la tarea:")
    descripcion = input("Ingrese la descripción de la tarea:")
    fecha_limite = input("Ingrese la fecha límite de la tarea:")
    prioridad = input("Ingrese la prioridad de la tarea:")
    
    lista_tareas.append([tarea, descripcion, fecha_limite, prioridad])
    
    print(lista_tareas)
    
    opcion = input("¿Desea agregar otra tarea? (Si/No):").lower()
    
    if opcion == "no":
        seguir = False
        
        
