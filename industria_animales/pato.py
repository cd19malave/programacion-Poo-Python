from animal import Animal


class Pato(Animal):
    def __init__(self, nombre, edad, tamano, color):
        super().__init__(nombre, edad, "laguna", "semillas e insectos", tamano, color)

    def moverse(self):
        return f"{self.nombre} nada y vuela corto"

    def comunicacion(self):
        return f"{self.nombre} se comunica con graznidos"
