class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.__promedio = promedio 

    def mostrar_datos(self):
        print(self.nombre)
        print(self.edad)
        print(self.__promedio)

    def get_promedio(self):
        return self.__promedio

    def set_promedio(self, nuevo):
        if 0 <= nuevo <= 10:
            self.__promedio = nuevo
        else:
            print("\nPromedio invalido.")

estudiante = Estudiante("Cristian", 19, 9.55)
estudiante.mostrar_datos()
estudiante.set_promedio(9.65)

estudiante.set_promedio(15)

print(estudiante.get_promedio())