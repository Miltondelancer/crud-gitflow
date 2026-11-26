from validar import validar_nombre

def crear_tarea(tareas):
    nombre = input("Nombre de la tarea: ")
    if validar_nombre(nombre):
        tareas.append(nombre)
        print("Tarea creada.")
