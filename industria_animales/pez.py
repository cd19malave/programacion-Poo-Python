from animal import Animal


class Pez(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "arrecife de coral", "algas y insectos", tamano, color)

    def moverse(self):
        return f"{self.nombre} nada entre los corales con sus aletas"

    def adaptacion(self):
        return f"{self.nombre} se adapta al agua con sus branquias y sus colores"
