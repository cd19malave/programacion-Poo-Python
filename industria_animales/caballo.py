from animal import Animal


class Caballo(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "campo verde", "hierba", tamano, color)

    def moverse(self):
        return f"{self.nombre} corre y salta en el campo"

    def comunicacion(self):
        return f"{self.nombre} se comunica con relinchos"
