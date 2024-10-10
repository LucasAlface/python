x = 3 
def somar(y=4): # função com 1 parâmetro que por definição é 4
    # global x # como usar a variável x que está fora da função, dentro da função
    x = 2 # este x é uma variável diferente da que está fora da função
    s = x + y # se não houver variável x dentro da função, mas se houver fora dela, a função usa o x fora da função, sem necessidade de usar um global
    print(s)

somar(x) # o x = 3 passa a ser o argumento, por isso o y da função passa a valer 3, então devolve 5
somar() # por definição o y vale 4, por isso devolve 6

def somar2(v1,v2=3,v3=None):
    if v3 is None: #so executa a funcao se v3="None"
        return v1 + v2 #se v3 for None faz v1 + v2
    else:
        return v1 + v2 + v3  #caso v3 seja algo diferente de "None" faz isso
s = somar2(8,10) #vai executar, v1=10, v2=10, caso metessemos um terceiro numero, faria o else porque v3!=None
q = somar2(8,10,10) #vai executar, v1=10, v2=10,v3=10 porque v3 ja tem valor
print(s)
print(q)

def somar3(*args):
    soma = 0
    for arg in args:
        soma = soma + arg
    return soma

def total_impares(*args):
    contagem = 0
    for arg in args:
        if arg % 2 == 1: # e impar
            contagem += 1
    return contagem

soma = lambda x,y: x + y
print(soma(3,2))
par = lambda x: "Par" if x % 2 == 0 else "Impar"

lista = [2, 3, 4]

# DOBRO DE UM NUM
dobro = map(lambda x: x * 2, lista)
print(list(dobro))

# AO INVES DE DAR 1,5 DA 1
metadeInteira = map(lambda x: x//2, lista)
print(list(metadeInteira))

# ELEVAR NUM A 2
quadrado = map(lambda x: x ** 2, lista)
print(tuple(quadrado))