# Este ficheiro vai ter as funções para o funcionamento do jogo

# Importações
import random
from classes import NaveAtual
from dicionarios import Cores # Dicionário com as cores
from colorama import Fore
import re # Correção do tamanho de strings com cor

# Variáveis globais
linhas_tabuleiro = 3 # Define quantas linhas tem o tabuleiro
num_jogadas = 0
tiros_dados = 0

Nave1 = NaveAtual("Aftonsparv", "GREEN", "A")
Nave2 = NaveAtual("Ikea", "CYAN", "B")
Nave3 = NaveAtual("Ikeia", "YELLOW", "C")    

Naves = [Nave1, Nave2, Nave3]


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
        largura_linha = comprimento_visivel(linha_formatada) + 1  # Contar o espaço extra para "|" e ajustamento do tamanho de elementos com cor
        espacos = (largura_maxima - largura_linha) // 2  # Calcula espaços para centralizar
        separador = (largura_linha)
        print(" " * espacos + linha_formatada + "|" + "\n" + " " * espacos + "-" * separador) # Para cada linha imprime o número de " " necessários para centralizar



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



# Método inserir as naves dentro do tabuleiro
def tabuleiro_naves(tabuleiro): 
    # Método que verifica se a posição está livre e coloca a nave caso esteja
    def colocar_nave(tabuleiro, nave):
        cor = Cores[nave.cor] # Transforma a cor da nave a um Fore. da respetiva cor
        nave.letra = f'{cor}{nave.letra}{Fore.RESET}' # Adiciona cor à letra da nave
        num_linha = random.randrange(linhas_tabuleiro) # Seleciona linha aleatoria do tabuleiro
        num_coluna = random.randrange(num_linha * 2 + 1) # Seleciona coluna aleatória dentro da linha escolhida
        if nave.energia > 0:
            if tabuleiro[num_linha][num_coluna] == ' ': # Verifica se a posição está disponível
                tabuleiro[num_linha][num_coluna] = nave.letra # Adição do elemento
            else:
                colocar_nave(tabuleiro, nave) # Repete a função caso a posição esteja ocupada
                
    
    # Inserção das naves    
    for nave in Naves:
        colocar_nave(tabuleiro, nave)
    return tabuleiro

# Método para inserir os tiros dentro da tabuleiro
# Mesma coisa que o método anterior, mas o elemento adicionado é diferente
def tabuleiro_tiros(tabuleiro): 
    def colocar_tiro(tabuleiro):
        num_linha = random.randrange(linhas_tabuleiro)
        num_coluna = random.randrange(num_linha * 2 + 1)
        if tabuleiro[num_linha][num_coluna] == ' ':
            tabuleiro[num_linha][num_coluna] = "X"
        else:
            colocar_tiro(tabuleiro)
            return num_linha, num_coluna
        
    for _ in range(3):
        colocar_tiro(tabuleiro)
    return tabuleiro

# Método para manter o comprimento normal pós coloração
def comprimento_visivel(texto):
    #Remove códigos ANSI e retorna o comprimento visível
    texto_sem_cor = re.sub(r'\033\[[0-9;]*m', '', texto) # Remove códigos ANSI
    return len(texto_sem_cor)

# Método para remover a energia
def remover_energia(tabuleiroNaves, tabuleiroTiros):
    def percorrer_tabuleiro(tabuleiroNaves, tabuleiroTiros, nave):
        for x in range(linhas_tabuleiro):
            h = x * 2 + 1
            for y in range(h):
                if tabuleiroNaves[x][y] == nave.letra and tabuleiroTiros[x][y] == "X":
                    nave.perda_energia()                                     
    for nave in Naves:   
        percorrer_tabuleiro(tabuleiroNaves, tabuleiroTiros, nave)
                           
   
def jogar(numJogadas, tirosDados):
    limpa_tela()
     
    tirosDados+=3
    
    tabuleiro = criar_tabuleiro(linhas_tabuleiro)
    tabuleiro2 = criar_tabuleiro(linhas_tabuleiro)
    
    tabuleiroNaves = tabuleiro_naves(tabuleiro)
    imprimir_tabuleiro(tabuleiroNaves)
    print("\n")
    tabuleiroTiros = tabuleiro_tiros(tabuleiro2)
    imprimir_tabuleiro(tabuleiroTiros)
    
    remover_energia(tabuleiroNaves, tabuleiroTiros)
    
    print(NaveAtual.Info(Nave1))
    print(NaveAtual.Info(Nave2))
    print(NaveAtual.Info(Nave3))
    print(tirosDados)
    
    
    
    
    numJogadas+=1
    print(numJogadas)
    
    if numJogadas < 30:
        input()
        jogar(numJogadas, tirosDados)
    else:
        print("Venceste o jogo!!!")
    
    
    
mostrar_capa()  
jogar(num_jogadas, tiros_dados)