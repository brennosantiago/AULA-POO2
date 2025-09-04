class Registro:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def __enter__(self):
        self.arquivo = open(self.caminho_arquivo, 'a')
        self.arquivo.write('Começo\n')
        return self.arquivo 

    def __exit__(self, tipo, valor, traceback):
        self.arquivo.write('Fim\n')
        self.arquivo.close()

if __name__ == "__main__":
    with Registro('log.txt') as f:
        f.write('Ok')
