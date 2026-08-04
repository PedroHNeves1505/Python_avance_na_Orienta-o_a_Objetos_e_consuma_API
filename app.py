from models.restaurante import Restaurante
from models.avaliacao import Avaliacao
from models.cardapio.bebidas import Bebidas
from models.cardapio.pratos import Pratos
from models.cardapio.sobremesas import Sobremesas

restaurante_penacony = Restaurante('Dreams Flavor', 'Sobremesas')
restaurante_amphoreus = Restaurante('Infinity Cycles', 'Rodízio')
restaurante_planacardia = Restaurante('Visionary Drinks', 'Bebidas alcólicas')
bebida_melancia = Bebidas('Suco de Melancia', 10.00, 'Grande')
bebida_melancia.aplicar_descontos()
prato_misto_quente = Pratos('Misto Quente', 9.00, 'Pão quentinho e tostado na manteiga por fora, recheado com queijo derretendo e presunto suculento por dentro.')
prato_misto_quente.aplicar_descontos()
cupcake = Sobremesas('Cupcake', 7.50, 'gelada', 'medio', 'Massa fofinha, cobertura cremosa e o tamanho perfeito para adoçar o dia.')
cupcake.aplicar_descontos()
restaurante_amphoreus.add_cardapio(bebida_melancia)
restaurante_amphoreus.add_cardapio(prato_misto_quente)
restaurante_amphoreus.add_cardapio(cupcake)

def main():
	restaurante_amphoreus.exibir_cardapio



if __name__ == '__main__':
	main()
	