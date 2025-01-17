# Este ficheiro vai ter as classes usadas para o jogo

from colorama import Fore, Style # Biblioteca com funções para adicionar cores
from dicionarios import Cores # Dicionário com as cores

# Super classe
class NaveModelo:
    def __init__(self, nome, cor, letra, perdaEnergia):
        self.nome = nome
        self.cor = cor
        self.energia = 100
        self.perdaEnergia = perdaEnergia
        self.letra = letra

    # Método para atualizar a energia
    def perda_energia(self):
        self.energia -= self.perdaEnergia
        if self.energia < 0:
            self.energia = 0
        return self.energia
    
    # Método para devolver a informação tratada
    def __str__(self):
        return f'Nome: {self.nome} Energia: {self.energia}% Letra: {self.letra}'

# Classe filho
class NaveAtual(NaveModelo):
    def __init__(self, nome, cor, letra, perdaEnergia, energiaExtra):
        super().__init__(nome, cor, letra, perdaEnergia)
        self.energiaExtra = energiaExtra 

    # Método que devolve a informação do método da super classe com a cor correspondente
    def Info(self):
        if self.cor in Cores:
            cor = Cores[self.cor] # Variável que vai ter o valor corresponte à chave do dicionáio que estiver no self.cor
            return f'{cor}{super().__str__()}{Style.RESET_ALL}' # Aplica a cor ao texto do método da super classe
        else:
            return f'{Fore.WHITE}{super().__str__()}{Style.RESET_ALL}' # Se a cor não for válida, usa branco por padrão

    # Método para adicioanr energia à nave
    def Add_Energia(self):
        self.energia += self.energiaExtra
        # Garante que a energia não ultrapassa os 100
        if self.energia > 100:
            self.energia = 100
        return self.energia
