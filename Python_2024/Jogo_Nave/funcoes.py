# Este ficheiro vai ter as funções para o funcionamento do jogo

import random
from classes import NaveModelo, NaveAtual

linhas_tabuleiro = 3 # Define quantas linhas tem o tabuleiro

# Função para definir o tabuleiro
def criar_tabuleiro(linhas):
    # Criar o tabuleiro como uma lista de listas
    tabuleiro = []
    for x in range(linhas):
        y = x * 2 + 1  # Função que define a quantidade de colunas que dada linha tem (y = colunas x = linha)
        linha = [" " for _ in range(y)]  # Inicializa cada linha com espaços
        tabuleiro.append(linha) # Adiciona os valores de cada linha

    return tabuleiro



# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    # Determinar o comprimento máximo para centralizar
    largura_maxima = (len(tabuleiro[-1]) * 4) + 4  # Verifica o tamanho da última linha do tabuleiro e multiplica por 4, porque cada coluna tem 4 caracteres "|  |" após a formatação

    for linha in tabuleiro:
        linha_formatada = "".join(f"| {coluna} " for coluna in linha)  # Junta com os separadores
        largura_linha = len(linha_formatada) + 1  # Contar o espaço extra para "|"
        espacos = (largura_maxima - largura_linha) // 2  # Calcula espaços para centralizar
        print(" " * espacos + linha_formatada + "|") # Para cada linha imprime o número de " " necessários para centralizar



# Método que faz 50 parágrafos para limpar a tela
def limpa_tela():
    print("\n" * 50)



# Método para criar a capa do início de jogo
def mostrar_capa():
    
    limpa_tela()
    
    capa = """
    ***********************************************
    *                                             *
    *          BEM-VINDO AO JOGO!                 *
    *                                             *
    ***********************************************
            ███╗   ██╗ █████╗ ██╗   ██╗███████╗
            ████╗  ██║██╔══██╗██║   ██║██╔════╝
            ██╔██╗ ██║███████║██║   ██║█████╗  
            ██║╚██╗██║██╔══██║╚██╗ ██╔╝██╔══╝  
            ██║ ╚████║██║  ██║ ╚████╔╝ ███████╗
            ╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝
    
    ***********************************************
    *  Pressione qualquer tecla para começar...   *
    ***********************************************
    """
    print(capa)
    
    input() # Aguarda que o utilizador pressione alguma tecla


tabuleiro = criar_tabuleiro(linhas_tabuleiro)


num_linha = random.randrange(linhas_tabuleiro)

num_coluna = random.randrange(num_linha * 2 + 1)

tabuleiro[num_linha][num_coluna] = "x"

imprimir_tabuleiro(tabuleiro)
    