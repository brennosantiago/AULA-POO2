class ListaDeTarefas:
    def __init__(self):
        self._tarefas = []

    def adicionar(self, tarefa):
        self._tarefas.append(tarefa)

    def remover(self, tarefa):
        self._tarefas.remove(tarefa)

    def __len__(self):
        return len(self._tarefas)

    def __getitem__(self, indice):
        return self._tarefas[indice]

    def __iter__(self):
        return iter(self._tarefas)

    def __str__(self):
        return f"ListaDeTarefas({self._tarefas})"

minha_lista = ListaDeTarefas()

minha_lista.adicionar("Arrumar a cama")
minha_lista.adicionar("Fazer exercícios")
minha_lista.adicionar("Ler um livro")

for tarefa in minha_lista:
    print("-", tarefa)
