from models.avaliacao import Avaliacao

class Restaurante:
	restaurantes = []
	
	def __init__(self, nome, categoria):
		self._nome = nome.title()
		self._categoria = categoria
		self._ativo = False
		self._avaliacoes = []
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
	