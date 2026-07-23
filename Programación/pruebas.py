materias = ["Calculo", "COE", "FFD", "Algebra lineal", "FP"]

asignatura = input("Ingrese la materia que desea saber si esta en la lista: ")

if asignatura in materias:
    print("Materia encontrada")
else:
    print("Materia no encontrada")
