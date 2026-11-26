def editar_tarea(tareas):
    if not tareas:
        print("No hay tareas para editar.")
        return
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")
    numero = int(input("Numero de la tarea a editar: "))
    if 1 <= numero <= len(tareas):
        tareas[numero - 1] = input("Nuevo nombre: ")
        print("Tarea editada.")
    else:
        print("Numero invalido.")
