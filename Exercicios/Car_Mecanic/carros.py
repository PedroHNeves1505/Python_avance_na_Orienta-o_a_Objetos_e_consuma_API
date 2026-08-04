from veiculos import Veiculos

class Carros(Veiculos):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor

    def __str__(self):
        return f'Marca: {self._marca} | Modelo: {self._modelo} | Cor: {self.cor}'

    def ligar(self):
        pass
    