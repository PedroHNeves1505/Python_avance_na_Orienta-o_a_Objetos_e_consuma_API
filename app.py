from models.restaurante import Restaurante
from models.avaliacao import Avaliacao
from models.cardapio.bebidas import Bebidas
from models.cardapio.pratos import Pratos

restaurante_penacony = Restaurante('Dreams Flavor', 'Sobremesas')
restaurante_amphoreus = Restaurante('Infinity Cycles', 'Rodízio')
restaurante_planacardia = Restaurante('Visionary Drinks', 'Bebidas alcólicas')
bebida_melancia = Bebidas('Suco de Melancia', 10.00, 'Grande')
prato_misto_quente = Pratos('Misto Quente', 9.00, 'Pão quentinho e tostado na manteiga por fora, recheado com queijo derretendo e presunto suculento por dentro. A combinação perfeita de crocância e sabor para qualquer hora do dia!')


def main():
	print(bebida_melancia)
	print(prato_misto_quente)



if __name__ == '__main__':
	main()
	