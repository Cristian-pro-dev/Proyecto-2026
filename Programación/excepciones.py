def sumar(a, b):
    suma = a + b
    print(suma)

def restar(a, b):
    resta = a - b
    print(resta)

def multiplicar(a, b):
    mul = a * b
    print(mul)

def dividir(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    else:
        print(division)
    finally:
        print("Operacion finalizada.")

def pedir_a():
    while True:
        try:
            a = int(input("Ingrese el primer numero: "))
            return a
        except ValueError:
            print("Solo puede ingresar numeros.")

def pedir_b():
    while True:
        try:
            b = int(input("Ingrese el segundo numero: "))
            return b
        except ValueError:
            print("Solo puede ingresar numeros.")

def menu():
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")

respuesta = "S"

while respuesta == "S":
    opcion = 0

    a = pedir_a()
    b = pedir_b()

    while opcion != 5:
        menu()
        try:
            opcion = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese un numero del menu.")

        if opcion == 1:
            sumar(a, b)
        elif opcion == 2:
            restar(a, b)
        elif opcion == 3:
            multiplicar(a, b)
        elif opcion == 4:
            dividir(a, b)
        elif opcion == 5:
            break
        else: print("Opcion invalida, ingrese de nuevo")   

    respuesta = input ("Desea ingresar nuevos numeros (S/N): ").upper()