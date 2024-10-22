def add(produto,preco,iva):
    return { 'product': produto, 'price': preco, 'tax': iva }

def update_final_price(dicion):
    dicion['final_price'] = round(dicion['price'] * ( 1 + dicion['tax']),2)

def print_product(p):
    print(f'{p['product']}; Preço: {p['price']};', sep='')
    print(f'Iva: {p['tax']*100}%, Preço final: {p['final_price']}'
    )