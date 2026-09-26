class Botella:
    def __init__(self, material, capacidad, forma, diseno, tapa, grabados):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseno = diseno
        self.tapa = tapa
        self.grabados = grabados

    def hacer_saludo(self, info_usuario):
        return f"Hola {info_usuario}"

    def contener_liquidos(self, liquido):
        return f"Contiene {liquido}"

    def facilitar_el_vertido(self):
        return "Facilita el vertido"

    def cerrar_hermetico(self):
        return "Tiene cierre hermetico"

    def transportar(self):
        return "Se puede transportar"

    def manejar(self):
        return "Es facil de manejar"

    def compatibilidad_con_bebidas(self, temperatura):
        return f"Es compatible con bebidas {temperatura}"

    def reutilizar(self):
        return "Se puede reutilizar"

    def transparencia(self):
        return "Es transparente"
