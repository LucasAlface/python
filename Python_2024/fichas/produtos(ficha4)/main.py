import produtos as p

products = []

# Adionar elementos à lista através do dicionário
products.append(p.add("Martelo", 15.45, 0.20))
products.append(p.add("Alicate", 12.50, 0.15))
products.append(p.add("Martelo", 15.45, 0.25))

for product in products:
    p.update_final_price(product)
    p.print_product(product)