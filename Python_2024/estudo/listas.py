import os

ferramentas = ['Alicate', 'Martelo', 'Chave de Fendas', 'Serra'] # criação de lista

# print(ferramentas[0]) # verificar posição da lista 0
ferramentas[2] = 'Parafusadeira' # substitui elemento da lista
# print(ferramentas[2]) # verificar a mudança
# print(ferramentas) # verficar lista inteira 
# print(type(ferramentas))

# Adicionar elemento no final da lista
ferramentas.append('Chave de Fendas')
print(ferramentas)

# Adcionar elemento em local espécifico da lista
ferramentas.insert(1, 'Furadeira') # 1 = posição na lista
print(ferramentas) 

# # Escreve a lista toda com um "x " antes de cada elemento e parágrafo entre cada elemento
# os.system("cls")
# for fr in ferramentas:
#     print(f'x {fr}') # O "f" indica que é uma f-string, que permite a formatação

# Escreve todos os elementos da lista que começam com "C"
# for fr in ferramentas:
#     if fr.startswith('C'):
#         print(f'x {fr}')

# # Escreve todos os elementos da lista que começam com "C" ou "P"
# for fr in ferramentas:
#     if fr.startswith(('C', 'P')): # o primeiro parênteses é a função "prefix" o outro parêntes é a tupla
#         print(f'x {fr}')

# Escreve a lista da posição 0 até à posição 6-1
# for i in range(6):
#     print(ferramentas[i])

# # Escreve a lista da posição 2 até à posição 5-1
# for x in range(2,5):
#     print(ferramentas[x])

# Remover o último elemento da lista
ferramentas.pop()
print(ferramentas)

# Remover elemento específico da lista
ferramentas.pop(2) # remove elemento de acordo com a posição da lista
print(ferramentas)

ferramentas.remove('Serra') # remove o primeiro elemento encontrado com o valor escolhido
print(ferramentas)
