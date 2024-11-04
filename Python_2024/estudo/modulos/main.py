import modules # Traz as funções, atributos e execuções do outro ficheiro
# import modules as m # Faz o mesmo, mas substitui o nome
# from modules import mult, soma # Importa funções ou atributos específicos do módulo
# import sys
from sys import platform

# O print(ola) do módulo também é executado

# Funções importadas
print(modules.soma(3,4))
print(modules.mult(3,4))

# Atributos importados
print(modules.Nome)

boasvindas = "Olá Python"

platform = "Minha plataforma"
# print(sys.platform) # o sys. só funciona se importarmos o módulo sys inteiro
print(platform) # O nosso atributo vai-se sobrepor ao atributo so sys que indica a plataforma do nosso computador
    