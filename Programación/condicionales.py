nombre = input("Introduzca nombre del estudiante: ")
calificacion = int(input("Introduzca su calificacion: "))

print("Alumno", nombre)
print("Su calificacion es", calificacion)

if 90 <= calificacion <= 100:
    print("Excelente")
elif 80 <= calificacion <= 89:
    print("Muy bien")
elif 70 <= calificacion <= 79:
    print("Bien")
elif 60 <= calificacion <= 69:
    print("Suficiente")
elif 0 <= calificacion < 60:
    print("Reprobado")
else:
    print("Calificacion invalida")