import json
from gravar_dados import nome_do_ficheiro
from pessoas import Pessoa

pessoas = []

# Leitura dos dados inseridos
with open(nome_do_ficheiro, 'r', encoding='utf8') as f: # O 'r' indica que vai ler o ficheiro
    pessoas = json.load(f) # O 'load' serve para ler e insere a leitura do ficheiro na lista 'pessoas'

for pessoa in pessoas:
    print(f'Nome: {pessoa['nome']}\nIdade: {pessoa['idade']}')



