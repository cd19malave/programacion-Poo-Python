from botella import Botella


class BotellaVidrio(Botella):
    def __init__(self, capacidad, forma, diseno, tapa, grabados):
        super().__init__("vidrio", capacidad, forma, diseno, tapa, grabados)

    def compatibilidad_con_bebidas(self, temperatura):
        return f"El vidrio aguanta bebidas calientes y frias ({temperatura})"

    def transparencia(self):
        return "El vidrio es totalmente transparente"
