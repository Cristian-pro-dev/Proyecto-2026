def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def pedir_a():
    a = int(input("Ingrese el primer numero: "))
    return a

def pedir_b():
    b = int(input("Ingrese el segundo numero: "))
    return b

def menu():
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")

respuesta = "S"

while respuesta == "S":
    opcion = 0

    a = pedir_a()
    b = pedir_b()

    while opcion != 5:
        menu()
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            suma = sumar(a, b)
            print(suma)
        elif opcion == 2:
            resta = restar(a, b)
            print(resta)
        elif opcion == 3:
            mul = multiplicar(a, b)
            print(mul)
        elif opcion == 4:
            if b == 0:
                print("No se puede dividir entre 0.")
            else:
                division = dividir(a, b)
                print(division)
        elif opcion == 5:
            break
        else: print("Opcion invalida, ingrese de nuevo")   

    respuesta = input ("Desea ingresar nuevos numeros (S/N): ").upper()

