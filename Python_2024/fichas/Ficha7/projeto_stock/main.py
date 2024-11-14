from stock import Stock
from produto import Produto

stock = Stock()

p1 = Produto("T-Shirt", 30, 5)
p2 = Produto("Calças", 80, 3)
p3 = Produto("Sapatos", 150, 2)

stock.adicionar_produto(p1)
stock.adicionar_produto(p2)
stock.adicionar_produto(p3)

print("Produtos em Stock:")
for dados in stock.listar_produtos():
    print(dados)

desconto = 10
produtos_com_desconto = stock.aplicar_desconto(desconto)

print(f"Produtos com Desconto de {desconto}%:")
for dados in produtos_com_desconto:
    print(dados.obter_dados())