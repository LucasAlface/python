class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def obter_dados(self):
        return f'Produto: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}'