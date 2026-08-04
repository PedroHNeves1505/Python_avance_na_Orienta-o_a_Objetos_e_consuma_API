from models.restaurante import Restaurante
from models.avaliacao import Avaliacao

restaurante_penacony = Restaurante('Dreams Flavor', 'Sobremesas')
restaurante_amphoreus = Restaurante('Infinity Cycles', 'Rodízio')
restaurante_planacardia = Restaurante('Visionary Drinks', 'Bebidas alcólicas')

Restaurante.alternar_estado(restaurante_amphoreus)
Restaurante.alternar_estado(restaurante_penacony)

restaurante_amphoreus.receber_avaliacao('Phainon', 4.3)
restaurante_amphoreus.receber_avaliacao('Mydei', 3.7)
restaurante_amphoreus.receber_avaliacao('Cyrene', 5.0)
restaurante_amphoreus.receber_avaliacao('Dan Heng', 2.0)
restaurante_amphoreus.receber_avaliacao('March 7th', 5.0)
restaurante_amphoreus.receber_avaliacao('Hysilens', 3.8)
restaurante_amphoreus.receber_avaliacao('Hyancine', 4.7)
restaurante_amphoreus.receber_avaliacao('Castorice', 4.8)
restaurante_amphoreus.receber_avaliacao('Tribbie', 1.5)
restaurante_amphoreus.receber_avaliacao('Aglea', 0.7)
restaurante_amphoreus.receber_avaliacao('Cifer', 8.0)

def main():
	Restaurante.listar_restaurantes()



if __name__ == '__main__':
	main()
	