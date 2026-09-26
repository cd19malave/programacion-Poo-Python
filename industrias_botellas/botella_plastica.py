from botella import Botella


class BotellaPlastica(Botella):
    def __init__(self, capacidad, forma, diseno, tapa, grabados):
        super().__init__("plastico", capacidad, forma, diseno, tapa, grabados)

    def compatibilidad_con_bebidas(self, temperatura):
        return f"El plastico solo aguanta bebidas {temperatura}"

    def transparencia(self):
        return "El plastico es poco transparente"
