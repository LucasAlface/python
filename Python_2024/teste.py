# print("kniga")
# print("Atenção")

# x = 2

# if x > 7:
#     print("yippie")
# elif x < 3:
#     print("womp womp")

# print(type(x)) # devolve o tipo de dado que a variável possuí no momento
x = "Stefan" # variável x passa de inteiro para string
n = 18 
#print(x)
#print(type(x))

# 3 formas diferentes de fazer a mesma coisa
# print("O meu nome é",x,"e a minha idade é",n)
# print("O meu nome é " + x + " e a minha idade é " + str(n))
# print(f'O meu nome é {x} e a minha idade é {n}')

# produto1 = "Martelo"
# produto2 = "Alicate"
# produto3 = "Tesoura"

# o fim da linha passa a ser um ", " em vez de passar para a próxima linha
# print(produto1,end=', ')
# print(produto2,end=', ')
# print(produto3)

import os # importa todas as funções od módulo
from random import randrange # importa a função randrange do módulo random

# escolhe um número aleatório entre 1 e 10
# num1 = randrange(1,10)
# print(num1)
# escolhe um número aleatório entre 1 e 20
# num2 = randrange(1,20)
# print(num2)

# num1 = int(input("Digite o primeiro valor: "))
# num2 = int(input("Digite o segundo valor: "))
# print("Soma =", num1+num2)

frase = "Maioria dos alunos"
print(frase[0:12]) # primeiros 11 carateres
print(frase[12:]) # do carater 12 até ao fim
print(len(frase)) # total de carateres na frase

frase = "Maioria dos alunos"
frase2 = frase.replace("Maioria","Minoria")
print(frase2)

lista_de_palavras = frase.split(" ")
print(type(lista_de_palavras))
print(lista_de_palavras)

for palavra in lista_de_palavras:
    print(palavra)

for i in range(10):
    print(i)
