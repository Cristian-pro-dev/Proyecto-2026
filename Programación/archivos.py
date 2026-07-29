respuesta = "S"

while respuesta == "S":
    nombre = input("Introduzca el nombre del estudiante: ")
    edad = int(input("Introduzca la edad del estudiante: "))
    carrera = input("Introduzca la carrera del estudiante: ")
    semestre = input("Introduzca el semestre del estudiante: ")

    with open("estudiantes.txt", "a") as archivo:
        archivo.write(f"\n{nombre} | {edad} | {carrera} | {semestre}")

    respuesta = input("Desea agregar a otro estudiante (S/N): ")

with open("estudiantes.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

    