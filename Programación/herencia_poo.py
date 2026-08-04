class Persona:

    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def presentarse(self):

        print("Hola, soy", self.nombre)

class Estudiante(Persona):

    def __init__(self, nombre, edad, carrera, semestre):

        super().__init__(nombre, edad)
        self.carrera = carrera
        self.semestre = semestre

    def estudiar(self):

        print(f"{self.nombre} estudia {self.carrera}")

class Profesor(Persona):

    def __init__(self, nombre, edad, especialidad):

        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def enseñar(self):

        print(f"{self.nombre} enseña {self.especialidad}")

alumno = Estudiante("Cristian", 19, "Ingenieria en IA", "Segundo") 
profesor = Profesor("Montiel", 59, "Matematicas Discretas")

alumno.presentarse()
profesor.presentarse()

alumno.estudiar()
profesor.enseñar()