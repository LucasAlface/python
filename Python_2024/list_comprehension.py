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

# Função que soma argumentos
def somar(*nums):
    soma = 0
    for num in nums:
        soma += num
    return soma
soma = somar(1,2,3)
print(soma)
