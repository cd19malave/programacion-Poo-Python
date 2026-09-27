class BotellaTermica:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados

    def llenar(self, liquido):
        return f"Botella llena de {liquido}"

    def servir(self):
        return f"Se sirve bien por su {self.forma}"

    def precintar(self):
        return f"Con la {self.tapa} queda bien cerrada"

    def llevar(self):
        return f"Cabe en la mochila porque es de {self.capacidad}"

    def sostener(self):
        return f"Se sostiene con una mano por su diseno {self.diseno}"

    def uso_en_bebidas(self, temperatura):
        return f"Funciona con bebidas {temperatura}"

    def reciclar(self):
        return f"Al final se recicla, sus grabados ({self.grabados}) son de {self.material}"

    def se_ve_el_liquido(self):
        return "Desde afuera se ve el liquido"
