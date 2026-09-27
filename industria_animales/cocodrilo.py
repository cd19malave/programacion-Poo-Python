from animal import Animal


class Cocodrilo(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "rio y laguna", "carne", tamano, color)

    def moverse(self):
        return f"{self.nombre} se arrastra y nada muy rapido"

    def adaptacion(self):
        return f"{self.nombre} se adapta al agua porque tiene los ojos arriba de la cabeza"
