from models.cardapio.item_cardapio import ItemCardapio

class Sobremesas(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self.tipo = tipo
        self.tamanho = tamanho
        self.descricao = descricao

    def __str__(self):
        return self._nome

    def aplicar_descontos(self):
        self._preco -= (self._preco * 0.03)