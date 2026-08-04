class Avaliacao:
	avaliacoes = []
	
	def __init__(self, cliente, nota):
		self._cliente = cliente
		self._nota = nota
	
	@property
	def cliente(self):
		return self.cliente
	
	@property
	def nota(self):
		return self.nota
	
