from pessoas import Pessoa
import json

nome_do_ficheiro = 'lista_pessoas.json'
pessoas = []

if __name__ == '__main__': # Só executa o código se for carregado através do próprio ficheiro e não executa caso seja importado

    # Inserção de pessoas na lista
    for i in range(3):
        nome = input(f'Escreva o nome da pessoa nº{i+1}: ')
        idade = int(input(f'Escreva a idade da pessoa nº{i+1}: '))
        pessoas.append(Pessoa(nome,idade).__dict__) # O __dict__ transforma a classe num dicionário

    # Criar ficheiro .json com os dados inseridos
    with open(nome_do_ficheiro, 'w', encoding='utf8') as f: # Cria o ficheiro 'lista_pessoas.json', o 'w' (write), indica que vai se escrever no ficheiro, utf8 é o tipo de codificação e permite acentos
        json.dump(pessoas,f,ensure_ascii=False,indent=2) # Escreve o que está dentro de pessoas como o 'f' (ficheiro), permite acentos e faz uma separação de 2 linhas

    print('Dados guardados com sucesso')



