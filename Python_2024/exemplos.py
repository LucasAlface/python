aluno = {
    'nome': 'Lucas Soares',
    'psi': 13.25,
    'port': 14.50,
    'mat': 11.33
}

def mediafinal(**valores):
    media = 0.0
    i = 0
    for disciplina, nota in valores.items():
        if isinstance(nota,float): # percorre o dicionario e pega apenas os valores do tipo float
            media += nota
            i += 1
    return media/i

m = mediafinal(**aluno)
print(m)

alunos = {
    'marcelo': {'nome': 'Marcelo Amorim', 'idade': 51},
    'ana': {'nome': 'Ana Abreu', 'idade': 53},
    'marta': {'nome': 'Marta Reis', 'idade': 19}
}

def maiorIdade(**als):
    mi = 0
    for al in als.values():
        if al['idade'] > mi:
            mi = al['idade']
    return mi

print(maiorIdade(**alunos))