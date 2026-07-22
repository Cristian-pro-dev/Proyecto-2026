respuesta = "S"

while respuesta == "S":
    suma = 0

    numero = int(input("Ingrese un numero: "))
    multiplo = int(input("Hasta que multiplo desea generar la tabla: "))

    for i in range(1, multiplo + 1):
        multiplicacion = numero * i
        print(f"{numero} x {i} = {multiplicacion}")
        suma += multiplicacion

    print("El mayor resultado de la tabla fue: ", multiplicacion)
    print("La suma de los resultado es: ", suma)
    respuesta = input("Desea generar otra tabla (S/N):")
