# Este ficheiro vai ter as funções para o funcionamento do jogo

# Função para definir o tabuleiro
def criar_tabuleiro(limite):
    # Criar o tabuleiro como uma lista de listas
    tabuleiro = []
    for x in range(limite):
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

# Exemplo de uso
limite = 3
tabuleiro = criar_tabuleiro(3)


# Acessando um espaço e preenchendo valores
tabuleiro[0][0] = "X"  # Linha 2, coluna 1
tabuleiro[2][4] = "O"  # Linha 3, coluna 3

# Imprimir o tabuleiro com os valores
imprimir_tabuleiro(tabuleiro)