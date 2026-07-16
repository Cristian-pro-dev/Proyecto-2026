nombre = input("Introduzca nombre del estudiante: ")
edad = int(input("Introduzca su edad: "))
carrera = input("Introduzca carrera: ")
calificacion = int(input("Introduzca su calificacion: "))

print("\nREPORTE DEL ESTUDIANTE")
print("\nAlumno:", nombre)
print("\nEdad:", edad)
print("\nCarrera:", carrera)
print("\nCalificacion:", calificacion)

if 90 <= calificacion <= 100:
    print("\nNivel : Excelente")
elif 80 <= calificacion <= 89:
    print("\nNivel: Muy bien")
elif 70 <= calificacion <= 79:
    print("\nNivel: Bien")
elif 60 <= calificacion <= 69:
    print("\nNivel: Suficiente")
elif 0 <= calificacion < 60:
    print("\nNivel: Reprobado")
else:
    print("\nCalificacion invalida")

if calificacion >= 60:
    print("\nEstado: Aprobado")
else:
    print("\nEstado: Reprobado")
