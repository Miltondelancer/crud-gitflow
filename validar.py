def validar_nombre(nombre):
    if nombre.strip() == "":
        print("El nombre no puede estar vacio.")
        return False
    return True
