nombre = input("Nombre: ")
peso = int(input("Peso: "))
altura = float(input("Altura: "))

imc = peso/(altura*altura)

print("Hola", nombre, "\n")
print("Tu IMC es: \n")
print(round(imc, 2))

print(f"\nHola {nombre}, tu IMC es {imc:.2f}")