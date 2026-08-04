class Veiculos:
    def __init__(self, marca, modelo, on_off):
        self._marca = marca
        self._modelo = modelo
        self._on_off = False

    def __str__(self):
        if self._on_off:
            return f'{self._modelo} da {self._marca} está ligado'
        else:
            return f'{self._modelo} da {self._marca} está desligado'