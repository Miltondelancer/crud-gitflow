def listar_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")
