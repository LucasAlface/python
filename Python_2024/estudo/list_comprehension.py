lista = []

# Lista de 1 a 10
lista_1 = [n for n in range(1,11)]

# Lista com a tabuada do 2
lista_2 = [n*2 for n in range(21)]

# Lista com apenas numeros pares
lista_3 = [
    num # Elementos da lista
    for num in range(21) #Elementos selecionados
    if num % 2 == 0 # Filtro dos elementos
]

# Soma elementos da lista
soma = sum([n for n in range(4)])
print(soma)

# Função que faz o mesmo que anterior
def somar(*nums):
    soma = 0
    for num in nums:
        soma += num
    return soma
soma = somar(1,2,3)
print(soma)

from statistics import mean
media = mean ([n for n in range(1,11)])
print (media)

produtos = [
    {"nome": "p1", "preco": 10 },
    {"nome": "p2", "preco": 20 },
    {"nome": "p3", "preco": 30 }
]

# Mapeamento
novos_produtos = [
    {**produto, "preco": produto["preco"] * 1.05} # Multiplica o preço do dicionario
    if produto["preco"] > 20 else {**produto} # Caso o preco seja maior que 20, caso contrário desempacota normalmente
    for produto in produtos # Faz isso para todos os dicionarios da lista
]

nums = [4,7,11,3,12,21]

nova_lista = [
    num if num > 10 else 0 # Mapear
    for num in nums
    if num > 11 # Filtrar
]

