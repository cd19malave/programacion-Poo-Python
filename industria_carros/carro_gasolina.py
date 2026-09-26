from carro import Carro


class CarroGasolina(Carro):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, "gasolina")

    def arrancar(self):
        self.encendido = True
        return f"El {self.modelo} arranca con {self.tipo_combustible}"

    def sistema_direccion(self, tipo):
        return f"El {self.modelo} usa direccion {tipo} (asistida por hidraulica)"
