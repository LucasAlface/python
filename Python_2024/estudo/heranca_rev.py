from colorama import Fore, Back
from getpass import getpass
from random import randrange, randint

print(Fore.RED + "Texto" + Fore.RESET) # Adciona cor ao texto

class Forma:
    def __init__(self,numLados,cor):
        self.numLados = numLados
        self.cor = cor

    def escrever(self):
        print(f'Metodo da classe Forma')

class Quadrado(Forma): # Chamar super classe
    def __init__(self, numLados, cor, diagonal):
        super().__init__(numLados, cor) # Atributos da super classe
        self.diagonal = diagonal

q = Quadrado(4, 'Azul', True)

q.escrever() # Objeto da classe filho pode chamar função da super classe