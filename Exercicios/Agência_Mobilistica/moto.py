from veiculos import Veiculos

class Moto(Veiculos):
    def __init__(self, marca, modelo, on_off, estilo):
        super().__init__(marca, modelo, on_off)
        self._estilo = estilo

    def __str__(self):
        texto_super = super().__str__()
        return f'Moto {texto_super} e é {self._estilo}'