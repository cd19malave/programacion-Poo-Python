class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamano = tamano
        self.color = color

    def moverse(self):
        return f"{self.nombre} se mueve"

    def comunicacion(self):
        return f"{self.nombre} se comunica con sonidos y olores"

    def reproduccion(self):
        return f"{self.nombre} se reproduce"

    def alimentarse(self):
        return f"{self.nombre} come {self.dieta}"

    def adaptacion(self):
        return f"{self.nombre} se adapta a su {self.habitat}"

    def instintos(self):
        return f"{self.nombre} tiene instintos de {self.dieta}"

    def descanso(self):
        return f"{self.nombre} descansa"

    def sueno(self):
        return f"{self.nombre} duerme varias horas al dia"

    def interaccion_social(self):
        return f"{self.nombre} convive con otros animales de su {self.habitat}"
