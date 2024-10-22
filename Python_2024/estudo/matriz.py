# Criação de Matriz
notas_alunos = [
    ["Marcelo", 12.5, 17.8],
    ["Ana", 13.25, 14],
    ["Rui", 17.25, 9.25],
    ["Leonor", 8.5, 10.25]
]

# Função que percorre a matriz e manipula-a para escrever a matriz da forma que quisermos
for linha in range(4): # 4 elementos da matriz
    for coluna in range(3): # 3 atributos de cada elemento 
        if coluna == 0: 
            print(notas_alunos[linha][coluna], end=": ") # o primeiro atributo (nome) vai ser sucedido por um ": "
        elif coluna == 1:
            print(notas_alunos[linha][coluna], end=", ") # o segundo atributo (primeira nota) vai ser sucedido por um ", "
        else:
            print(notas_alunos[linha][coluna]) # o terceiro atributo (segunda nota) é o último atributo, não precisa de sucessão

# outras formas de fazer a mesma coisa
for c1,c2,c3 in notas_alunos:
    print(f'{c1}: {c2}, {c3}')

for linha in notas_alunos:
    print(f'{linha[0]}: {linha[1]}, {linha[2]}')