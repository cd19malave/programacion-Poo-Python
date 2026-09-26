class Carro:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.numero_puertas = numero_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible
        self.encendido = False
        self.velocidad = 0

    def arrancar(self):
        self.encendido = True
        return f"El {self.modelo} arranca"

    def apagar(self):
        self.encendido = False
        self.velocidad = 0
        return f"El {self.modelo} se apaga"

    def acelerar(self, velocidad):
        self.velocidad += velocidad
        return f"El {self.modelo} acelera a {self.velocidad} km/h"

    def frenar(self, velocidad):
        self.velocidad -= velocidad
        return f"El {self.modelo} frena y queda a {self.velocidad} km/h"

    def climatizacion(self, estado):
        return f"Climatizacion {estado}"

    def sistema_direccion(self, tipo):
        return f"Sistema de direccion {tipo}"

    def tipo_seguridad(self):
        return "Cinturon de seguridad y airbags"

    def luces(self, estado):
        return f"Luces {estado}"

    def sistema_ventanas(self, estado):
        return f"Ventanas {estado}"

    def sistema_espejo(self, estado):
        return f"Espejos {estado}"
