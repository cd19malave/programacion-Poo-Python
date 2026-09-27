from botella_termica import BotellaTermica


class TermicaVidrio(BotellaTermica):
    def __init__(self, capacidad, forma, diseno, tapa, grabados):
        super().__init__("vidrio", capacidad, forma, diseno, tapa, grabados)

    def uso_en_bebidas(self, temperatura):
        return f"El vidrio aguanta bebidas {temperatura} sin romperse"

    def se_ve_el_liquido(self):
        return "Con el vidrio se ve el liquido"
