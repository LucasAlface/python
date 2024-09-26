# várias formas de fazer a mesma coisa

lista = [1, 2, 3]
lista2 = lista
print(lista2)

a=1
b=2
c=3

a,b,c=1,2,3
a,b,c = lista
print(a,b,c)

tupla = ('a', 'b')
# tupla[0] = 'c' # Não é possível alterar uma tupla
print(tupla)

# Alterar valor de uma tupla
l = list(tupla) # Cria uma lista da tupla
l[0] = 'c' # Altera valor da lista
tupla = tuple(l) # A lista passa a ser a tupla
print(tupla) # verficar alteração