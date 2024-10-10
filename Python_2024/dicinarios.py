aluno = {
    'nome': 'Lucas',
    'nota_matematica': 18.5,
    'nota_portugues': 17,
    'outras_notas': [13, 14, 25, 17,5, 8.25]
}

print(aluno['outras_notas'][1])

for k in aluno: # Imprime a chave
    print(k)

for v in aluno.values(): # Imprime os valores
    print(v)

for k,v in aluno.items(): # Imprime a chave seguido do valor associado
    print(f'{k}: {v}')