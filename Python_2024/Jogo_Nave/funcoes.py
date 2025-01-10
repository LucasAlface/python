# Este ficheiro vai ter as funções para o funcionamento do jogo

# Importações
import random
from classes import NaveAtual
from dicionarios import Cores # Dicionário com as cores
from colorama import Fore
import re # Correção do tamanho de strings com cor

# Variáveis globais
linhas_tabuleiro = 3 

# Objetos
Nave1 = NaveAtual("Aftonsparv", "GREEN", "A", 14, 100)
Nave2 = NaveAtual("Ikea", "CYAN", "B", 12, 35)
Nave3 = NaveAtual("Ikeia", "YELLOW", "C", 10, 20)    

# Lista com os objetos
Naves = [Nave1, Nave2, Nave3]


# ****************** FUNÇÕES E MÉTODOS ******************


# Método para criar a capa do início de jogo
def capa():   
    limpa_tela()
    print( """
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
    """)
    
    input() # Aguarda que o utilizador pressione alguma tecla

# Método com mensagem de vitória     
def vencer():
    limpa_tela()
    print(""" 
                  
____    ____  _______ .__   __.   ______  _______      _______..___________. _______  __   __   __  
\   \  /   / |   ____||  \ |  |  /      ||   ____|    /       ||           ||   ____||  | |  | |  | 
 \   \/   /  |  |__   |   \|  | |  ,----'|  |__      |   (----``---|  |----`|  |__   |  | |  | |  | 
  \      /   |   __|  |  . `  | |  |     |   __|      \   \        |  |     |   __|  |  | |  | |  | 
   \    /    |  |____ |  |\   | |  `----.|  |____ .----)   |       |  |     |  |____ |__| |__| |__| 
    \__/     |_______||__| \__|  \______||_______||_______/        |__|     |_______|(__) (__) (__) 
                                                                                                    

    """)

# Método com mensagem de derrota   
def perder():
    limpa_tela()
    print(""" 
          
     ___        ______      ___      .______     ______    __    __          ___
    /   \      /      |    /   \     |   _  \   /  __  \  |  |  |  |     _  /  /
   /  ^  \    |  ,----'   /  ^  \    |  |_)  | |  |  |  | |  |  |  |    (_)|  | 
  /  /_\  \   |  |       /  /_\  \   |   _  <  |  |  |  | |  |  |  |       |  | 
 /  _____  \  |  `----. /  _____  \  |  |_)  | |  `--'  | |  `--'  |     _ |  | 
/__/     \__\  \______|/__/     \__\ |______/   \______/   \______/     (_)|  | 
                                                                            \__\ 

    """)

# Método que faz 50 parágrafos para limpar a tela
def limpa_tela():
    print("\n" * 50)

# Função para definir o tabuleiro
def criar_tabuleiro(linhas):
    # Criar o tabuleiro como uma lista de listas
    tabuleiro = []
    for x in range(linhas):
        y = x * 2 + 1  # Função que define a quantidade de colunas que dada linha tem (y = quantidade de colunas; x = linha)
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
    return largura_maxima # Devolve para poder fazer separação com os mesmos "-" em outras partes do código

# Função que devolve o comprimento da string sem cor
def comprimento_visivel(texto):
    # Remove códigos ANSI e retorna o comprimento visível
    texto_sem_cor = re.sub(r'\033\[[0-9;]*m', '', texto) # Remove códigos ANSI
    return len(texto_sem_cor)


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


# Método para remover a energia
def remover_energia(tabuleiroNaves, tabuleiroTiros):
    tiros_acertados = 0
    def percorrer_tabuleiro(tabuleiroNaves, tabuleiroTiros, nave):
        tiros_certeiros = 0
        for x in range(linhas_tabuleiro):
            h = x * 2 + 1
            for y in range(h):
                if tabuleiroNaves[x][y] == nave.letra and tabuleiroTiros[x][y] == "X":
                    tiros_certeiros += 1 # Adiciona tiro caso nave seja atingida
                    nave.perda_energia()
        return tiros_certeiros                                                      
     
    for nave in Naves:     
        tiros_acertados += percorrer_tabuleiro(tabuleiroNaves, tabuleiroTiros, nave)
    return tiros_acertados # Devolve quantos tiros foram acertados na ronda

# Método para recomeçar ou fechar o jogo após o término    
def recomecar():
    print("Clique 1 para recomeçar, clique 2 para fechar")
    escolha = input()
    if escolha == "1":
        for nave in Naves:
            nave.energia = 100 # Reseta energia das naves
        jogar(0,0) # Recomeça o jogo do zero
    if escolha == "2":
        exit() # Fecha programa
    else:
        print("Escolha uma opção válida!")
        recomecar() # Recursividade                       

# Método que executa os métodos criados para fazer o jogo   
def jogar(tirosDados, totalTirosAcertados):
    while tirosDados < 105:  # Continua enquanto o jogador não ultrapassa 105 tiros
        # *** RONDA ***
        limpa_tela()

        tirosDados += 3 # Contador do total de tiros

        # Declaração dos 2 tabuleiros
        tabuleiro = criar_tabuleiro(linhas_tabuleiro)
        tabuleiro2 = criar_tabuleiro(linhas_tabuleiro)

        # Print do tabuleiro com as naves
        tabuleiroNaves = tabuleiro_naves(tabuleiro)
        espacos = imprimir_tabuleiro(tabuleiroNaves) # Quantidade de "-" para separar por estética
        print("\n") # Separação entre tabuleiros
        # Print do tabuleiro com os tiros
        tabuleiroTiros = tabuleiro_tiros(tabuleiro2)
        imprimir_tabuleiro(tabuleiroTiros)

        # Remoção de energia das naves
        tirosAcertados = remover_energia(tabuleiroNaves, tabuleiroTiros) # Quantos tiros foram acertados na ronda
        totalTirosAcertados += tirosAcertados # Contador do total de tiros acertados

        # Dados atuais das naves
        for nave in Naves:
            print(NaveAtual.Info(nave))

        print("-" * espacos) # Separação estética
        
        # Estatísticas
        Informacao = (f"{Fore.MAGENTA}Tiros dados: {tirosDados}\nTiros acertados: {totalTirosAcertados}(+{(tirosAcertados)})\nEficácia de tiro: {round(totalTirosAcertados * 100 / tirosDados, 2)}%{Fore.RESET}")
        print(Informacao)
        
        # Verifica se o jogador ganhou
        if all(nave.energia == 0 for nave in Naves):
            vencer()
            imprimir_tabuleiro(tabuleiroNaves)
            imprimir_tabuleiro(tabuleiroTiros)
            print(Informacao)
            recomecar() # Jogo terminado pergunta se quer recomeçar

        # Adiciona energia às naves depois de 45 tiros
        if tirosDados == 45:
            for nave in Naves:
                if nave.energia > 0:
                    nave.Add_Energia()
        
        
        print("-" * espacos) # Separação estética
        input(f"{Fore.RED}Clique Enter para continuar...{Fore.RESET}") # Começa nova ronda
        # *** FIM DA RONDA ***

    # Condição de derrota
    perder()
    imprimir_tabuleiro(tabuleiroNaves)
    imprimir_tabuleiro(tabuleiroTiros)
    print(Informacao)
    recomecar() # Jogo terminado pergunta se quer recomeçar

        
    
    


