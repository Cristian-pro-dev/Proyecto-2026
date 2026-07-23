respuesta = "S"

while respuesta == "S":
    materias = []
    cantidad = int(input("Cuantas materias desea ingresar: "))

    for i in range(cantidad):
        materias.append(input("Ingrese la materia: "))

    respuesta = input("Desea buscar una materia en la lista (S/N): ").upper()
    if respuesta == "S":
        asignatura = input("Ingrese la materia: ")
        if asignatura in materias:
            print("La materia si pertenece a la lista")
        else:
            print("La materia no pertenece a la lista")

    respuesta = input("Desea modificar alguna materia (S/N): ").upper()
    if respuesta == "S":
        asignatura = input("Ingrese la materia: ")
        for i in range(len(materias)):
            if materias[i] == asignatura:
                materias[i] = input("Ingrese la nueva materia: ")
                break

    print(materias)
    print("Total de materias registradas:", len(materias))

    respuesta = input("Desea ingresar otra lista (S/N): ").upper()
