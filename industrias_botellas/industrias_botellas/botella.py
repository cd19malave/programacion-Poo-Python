class Botella:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados

    def contener_liquidos(self, liquido):
        return f"Contiene {liquido}"

    def facilitar_el_vertido(self):
        return f"Facilita el vertido por su forma de {self.forma}"

    def cerrar_hermetico(self):
        return f"Cierre hermetico con {self.tapa}"

    def transportar(self):
        return f"Se transporta bien, pesa poco y mide {self.capacidad}"

    def manejar(self):
        return f"Se maneja facil por su diseno {self.diseno}"

    def compatibilidad_con_bebidas(self, temperatura):
        return f"Es compatible con bebidas {temperatura}"

    def reutilizar(self):
        return f"Se puede reutilizar, sus grabados ({self.grabados}) no se borran"

    def transparencia(self):
        return "Deja ver el liquido que contiene"
