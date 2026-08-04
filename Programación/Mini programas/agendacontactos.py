def menu():
    print("\n1. Agregar contacto\n2. Buscar contacto\n3. Eliminar contacto\n4. Modificar telefono\n5. Mostrar contactos\n6. Salir")

def agregar():
    nombre = input("Introduzca el nombre del contacto: ")
    numero = int(input("Introduzca el numero del contacto: "))

    contacto = {
        "nombre" : nombre,
        "telefono" : numero
    }

    contactos.append(contacto)

def buscar():
    bandera = False
    op = input("Ingrese el nombre del contacto: ")
    for contacto in contactos:
        if contacto["nombre"] == op:
            print("Contacto encontrado:")
            print(f"Nombre: {contacto["nombre"]}")
            print(f"Telefono: {contacto["telefono"]}")
            bandera = True
            break

    if bandera == False:
        print("Contacto no encontrado.")

def eliminar():
    bandera = False
    op = input("Ingrese el nombre del contacto: ")
    for contacto in contactos:
        if contacto["nombre"] == op:
             contactos.remove(contacto)
             bandera = True
             break

    if bandera == False:
        print("Contacto no encontrado.")

def modificar():
    bandera = False
    op = input("Ingrese el nombre del contacto: ")
    for contacto in contactos:
        if contacto["nombre"] == op:
            contacto["telefono"] = int(input("Ingrese el nuevo numero: "))
            bandera = True
            break
    
    if bandera == False:
        print("Contacto no encontrado.")

def mostrar():
    for contacto in contactos:
        print(f"Nombre: {contacto["nombre"]}")
        print(f"Telefono: {contacto["telefono"]}")

opcion = 0
contactos = []

while opcion != 6:
    print("\nSISTEMA DE REGISTRO DE CONTACTOS")
    menu()
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        agregar()
    elif opcion == 2:
        buscar()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        modificar()
    elif opcion == 5:
        mostrar()
    elif opcion == 6:
        break
    else: print("Opcion invalida, ingrese de nuevo")   





