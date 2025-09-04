class Livro:
    def __init__(self, titulo, autor, estoque):
        self._titulo = titulo
        self._autor = autor
        self._estoque = estoque
    
    @property    
    def estoque(self):
        return self._estoque
        
    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            raise ValueError ("Estoque não pode ser negativo.")
        self._estoque = valor
        
teste = Livro("Clean Code", "Joaozinho", 2)
print(teste.estoque)

teste.estoque = -1
print(teste.estoque)
