respuesta = "S"

while respuesta == "S":
    cantidad = 0
    suma = 0
    contador = 0

    while contador < 7:
        cantidad = int(input("Ingrese su ahorro del dia: "))
        while cantidad < 0:
            print("Cantidad invalida, ingrese de nuevo la cantidad")
            cantidad = int(input("Ingrese su ahorro del dia: "))

        suma += cantidad 
        contador += 1

    print("Total ahorrado: \n", suma)
    if suma >= 500:
        print("Excelente ahorro")

    print("Promedio: \n", suma/7)

    respuesta = input("Desea registrar otra semana (S/N): ")