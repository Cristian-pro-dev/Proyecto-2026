class Usuario:

    def mostrar_panel(self):
        print("Informacion del usuario")

class Alumno(Usuario):

    def mostrar_panel(self):
        print("Soy alumno de Ingenieria en IA en el IPN")

class Profesor(Usuario):

    def mostrar_panel(self):
        print("Soy profesor de calculo del IPN")

class Administrador(Usuario):

    def mostrar_panel(self):
        print("Soy administrador del SAES en el IPN")

alumno = Alumno()
profesor = Profesor()
administrador = Administrador()

usuarios = [alumno, profesor, administrador]

for usuario in usuarios:
    usuario.mostrar_panel()

