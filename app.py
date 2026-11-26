from crear import crear_tarea
from listar import listar_tareas
from editar import editar_tarea
from eliminar import eliminar_tarea

tareas = []

def menu():
    while True:
        print("\n1. Crear tarea")
        print("2. Listar tareas")
        print("3. Editar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            crear_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            editar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            break
        else:
            print("Opcion invalida.")

menu()
