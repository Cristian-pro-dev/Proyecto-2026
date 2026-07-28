def menu():
    print("\n1. Mostrar informacion\n2. Modificar dato\n3. Agregar nuevo dato\n4. Eliminar dato\n5. Salir")

def mostrar():
    for clave, valor in estudiante.items():
        print(clave, ":", valor)

def modificar():
    opcion = input("Ingrese el dato que quiere modificar: ")
    if opcion in estudiante:
        estudiante[opcion] = input("Nuevo valor: ")
    else:
        print("Ese dato no existe.")

def agregar():
    opcion = input("Ingrese el dato que quiere agregar: ")
    if opcion in estudiante:
        print("Ese dato ya existe.")
    else:
        estudiante[opcion] = input("Introduzca el valor del nuevo dato: ")

def eliminar():
    opcion = input("Ingrese el dato que quiere eliminar: ")
    if opcion in estudiante:
        del estudiante[opcion]
    else:
        print("Ese dato no existe.")

respuesta = "S"

while respuesta == "S":
    op = 0

    nombre = input("Introduzca el nombre del estudiante: ")
    edad = int(input("Introduzca la edad del estudiante: "))
    carrera = input("Introduzca la carrera del estudiante: ")
    semestre = input("Introduzca el semestre del estudiante: ")
    promedio = float(input("Introduzca el promedio del estudiante: "))

    estudiante = {
        "nombre" : nombre,
        "edad" : edad,
        "carrera" : carrera,
        "semestre" : semestre,
        "promedio" : promedio
    }

    while op != 5:
        menu()
        op = int(input("Seleccione una opcion: "))

        if op == 1:
            mostrar()
        elif op == 2:
            modificar()
        elif op == 3:
            agregar()
        elif op == 4:
            eliminar()
        elif op == 5:
            break
        else: print("Opcion invalida, ingrese de nuevo")   

    respuesta = input ("Desea ingresar nuevos datos (S/N): ").upper()