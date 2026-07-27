def promedio(lista):
    return sum(lista) / len(lista)

promedio = promedio([2, 3, 4, 5])

if promedio >= 6:
    print("Aprobado")
else:
    print("Reprobado")