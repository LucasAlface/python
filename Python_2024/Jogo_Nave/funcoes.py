
# Este ficheiro vai ter as funções para o funcionamento do jogo

import random
from classes import NaveModelo, NaveAtual
from dicionarios import Cores # Dicionário com as cores
from colorama import Fore

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
    largura_maxima = (len(tabuleiro[-1]) * 4) + 1  # Verifica o tamanho da última linha do tabuleiro e multiplica por 4, porque cada coluna tem 4 caracteres "|  |" após a formatação

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
tabuleiro2 = criar_tabuleiro(linhas_tabuleiro)



Nave1 = NaveAtual("Alien", "GREEN", "A")
Nave2 = NaveAtual("Mirtilo", "CYAN", "B")
Nave3 = NaveAtual("Caramelo", "YELLOW", "C")


def tabuleiro_naves(tabuleiro, nave1, nave2, nave3): 
    def colocar_nave(tabuleiro, nave):
        cor = Cores[nave.cor]
        nave.letra = f'{cor}{nave.letra}{Fore.RESET}'
        num_linha = random.randrange(linhas_tabuleiro)
        num_coluna = random.randrange(num_linha * 2 + 1)
        if tabuleiro[num_linha][num_coluna] == ' ':
            tabuleiro[num_linha][num_coluna] = nave.letra
        else:
            colocar_nave(tabuleiro, nave)
            return num_linha, num_coluna
        
    colocar_nave(tabuleiro, nave1)
    colocar_nave(tabuleiro, nave2)
    colocar_nave(tabuleiro, nave3)
    return tabuleiro

def tabuleiro_tiros(tabuleiro): 
    def colocar_tiro(tabuleiro):
        num_linha = random.randrange(linhas_tabuleiro)
        num_coluna = random.randrange(num_linha * 2 + 1)
        if tabuleiro[num_linha][num_coluna] == ' ':
            tabuleiro[num_linha][num_coluna] = "X"
        else:
            colocar_tiro(tabuleiro)
            return num_linha, num_coluna
        
    colocar_tiro(tabuleiro)
    colocar_tiro(tabuleiro)
    colocar_tiro(tabuleiro)
    return tabuleiro



tabuleiroNaves = tabuleiro_naves(tabuleiro, Nave1, Nave2, Nave3)
imprimir_tabuleiro(tabuleiroNaves)
tabuleiroTiros = tabuleiro_tiros(tabuleiro2)
imprimir_tabuleiro(tabuleiroTiros)

    
