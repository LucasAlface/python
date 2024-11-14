from Classes import Aluno
import json

nome_do_ficheiro = 'Lista_Alunos.json'

def salvar_alunos(alunos):
    with open(nome_do_ficheiro, 'w', encoding='utf8') as f: # Cria o ficheiro 'Lista_Alunos.json', o 'w' (write), indica que vai se escrever no ficheiro, utf8 é o tipo de codificação e permite acentos
            json.dump([aluno.__dict__ for aluno in alunos], f) # Transforma a lista enviada num dicionário e escreve como o 'f' (ficheiro), permite acentos e faz uma separação de 2 linhas

# Leitura dos dados inseridos
def carregar_alunos():
    with open(nome_do_ficheiro, 'r', encoding='utf8') as f: # O 'r' indica que vai ler o ficheiro
        alunos_data = json.load(f) # O 'load' serve para ler e insere a leitura do ficheiro na lista 'alunos'

    return [Aluno(**dados) for dados in alunos_data] # Cria uma lista de objetos Aluno a partir dos dados carregados