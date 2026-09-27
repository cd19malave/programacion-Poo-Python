from animal import Animal


class Escarabajo(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "suelo del bosque", "hojas y madera", tamano, color)

    def moverse(self):
        return f"{self.nombre} camina y vuela con su caparazon"

    def instintos(self):
        return f"{self.nombre} tiene el instinto de esconder sus cosas"
