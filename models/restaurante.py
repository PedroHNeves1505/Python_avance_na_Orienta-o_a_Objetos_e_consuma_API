from models.avaliacao import Avaliacao
from models.cardapio.item_cardapio import ItemCardapio
class Restaurante:
	restaurantes = []
	
	def __init__(self, nome, categoria):
		self._nome = nome.title()
		self._categoria = categoria
		self._ativo = False
		self._avaliacoes = []
		self._cardapio = []
		Restaurante.restaurantes.append(self)
		
	def __str__(self):
		return f'Nome: {self._nome} | Categoria: {self._categoria}'
	
	@classmethod
	def listar_restaurantes(cls):
		print(f'{"Nome".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | Ativo')
		for restaurante in cls.restaurantes:
			print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante.ativo}')
	
	@property
	def ativo(self):
		return '☑'if self._ativo else '☐'
	
	@property
	def nome(self):
		return self._nome
	
	@property
	def categoria(self):
		return self._categoria

	def alternar_estado(self):
		self._ativo = not self._ativo
	
	def receber_avaliacao(self, cliente, nota):
		if 0 < nota <= 5:	
			avaliacao = Avaliacao(cliente, nota)
			self._avaliacoes.append(avaliacao)

	
	@property
	def media_avaliacao(self):
		if not self._avaliacoes:
			return 'N/A'
		soma_avaliacao = sum(avaliacoes._nota for avaliacoes in self._avaliacoes)
		qnt_notas = len(self._avaliacoes)
		media = round(soma_avaliacao / qnt_notas, 1)
		if qnt_notas < 10:
			return 'N/A'
		else:
			return media

	def add_cardapio(self, item):
		if isinstance(item, ItemCardapio):
			self._cardapio.append(item)

	@property
	def exibir_cardapio(self):
		print(f'Cardapio do Restaurante {self._nome}\n')
		for i,item in enumerate(self._cardapio,start=1):
			if hasattr(item, 'descricao'):
				mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
				print(mensagem_prato)
			else:
				mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
				print(mensagem_bebida)