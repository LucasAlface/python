from produto import Produto

class Stock:
    def __init__(self):
        self.lista_de_produtos = []

    def adicionar_produto(self, produto):
        self.lista_de_produtos.append(produto)

    def listar_produtos(self):
        return [produto.obter_dados() for produto in self.lista_de_produtos]
    
    def aplicar_desconto(self, desconto):
        return list(map(lambda p: Produto(p.nome, p.preco * (1 - desconto / 100), p.quantidade), self.lista_de_produtos))
    
    def lista_produtos_stock_baixo(self, valor):
        return [produto for produto in self.lista_de_produtos if produto.quantidade < valor]