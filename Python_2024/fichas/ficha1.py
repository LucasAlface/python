#EX1
def somar (*args):
    soma = 0
    for arg in args:
        if 5 < arg < 10:
            soma = soma + arg
    return soma         
print (somar(7,8,9))
#EX2
positivo_negativo = lambda n: "P" if n > 0 else "N"
print(positivo_negativo(5))

#EX3
def inversor(num):
    inverso = 0
    while num != 0:
        inverso = inverso * 10 + num % 10
        num = num // 10
    return inverso

print(inversor(127))


#EX4
contar_digitos = lambda num: len(str(num))
numero = int(input("Digite um valor: "))
print(contar_digitos(numero))

#EX5
def perfeito(num):
    soma = 0
    for divisor in range (1,num):
        if num % divisor == 0:
            soma = soma + divisor
    if num == soma:
        print("Perfeito")
    else:
        print("Imperfeito")

perfeito(6)
perfeito(7)
perfeito(93)
perfeito(28)