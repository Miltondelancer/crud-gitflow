def eliminar_tarea(tareas):
    if not tareas:
        print("No hay tareas para eliminar.")
        return
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")
    numero = int(input("Numero de la tarea a eliminar: "))
    if 1 <= numero <= len(tareas):
        tareas.pop(numero - 1)
        print("Tarea eliminada.")
    else:
        print("Numero invalido.")
