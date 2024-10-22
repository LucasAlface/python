# EX1
num_pares = [
    num # Elementos da lista
    for num in range(1,11) #Elementos selecionados
    if num % 2 == 0 # Filtro dos elementos
]
print(num_pares)

# EX2
num_quadrado = [n*n for n in range (1,11)]
print(num_quadrado)

# EX3
palavras = ["zunga", "zezo", "sopas"]
tam_palavra = [
    len(p)
    for p in palavras
]
print(tam_palavra)


# EX4
nums = [1,2,3,4,5,6,7,8,9,10]
nova_lista = [
    num
    for num in nums
    if num > 5 # Filtrar
]
print(nova_lista)

# EX5
nome = "Lucas Soares"
novo_nome = [
    char for char in nome if char.isupper()
]
print(novo_nome)

# EX6
nums = [1,2,3,4,5,6,7,8,9]
novos_num = [  
    num*2 if num % 3 == 0 else num
    for num in nums
]
print(novos_num)

# EX7
nome = ["Lucas", "Alexandre", "Afonso", "Filipe"]
nome_a = [
    k.upper() for k in nome if 'A' in k
]
print(nome_a)

# EX8
fruta = ["Banana", "Maca", "Laranja", "Pera"]
fruta_comp = [
    len(comp) if len(comp) > 5 else 0 
    for comp in fruta
    ]
print(fruta_comp)