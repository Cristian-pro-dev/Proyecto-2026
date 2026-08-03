class Estudiante:

    def __init__(self, nombre, edad, carrera, semestre, promedio):

        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.semestre= semestre
        self.promedio = promedio

    def mostrar_datos(self):

        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Carrera:", self.carrera)
        print("Semestre:", self.semestre)
        print("Promedio:", self.promedio)

    def actualizar_promedio(self):

        self.promedio = float(input("Ingrese el nuevo promedio del estudiante: "))

    def actualizar_semestre(self):
    
        self.semestre = input("Ingrese el nuevo semestre del estudiante: ")

alumno_uno = Estudiante ("Cristian", 19, "IA", "Segundo", 9.5)
alumno_dos = Estudiante ("Ana", 20, "ISC", "Tercero", 8.7)

alumno_uno.mostrar_datos()
alumno_dos.mostrar_datos()

alumno_uno.actualizar_promedio()
alumno_dos.actualizar_semestre()

alumno_uno.mostrar_datos()
alumno_dos.mostrar_datos()