from veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, marca, modelo, on_off, portas):
        super().__init__(marca, modelo, on_off)
        self._portas = portas

    def __str__(self):
        texto_super = super().__str__()
        return f'Carro {texto_super} e possui {self._portas} portas'