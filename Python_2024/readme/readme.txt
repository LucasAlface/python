ESTUDO

teste.py
Introdução a definição de variáveis, manipulação de variáveis e uso de funções básicas.

listas.py
Criação e manipulação de listas.

tuplas.py
Diferenças entre listas e tuplas, demonstração que tuplas são intocáveis, conversão de tuplas a listas e vice-versa

matriz.py
Criação e manipulação de matrizes

dicinarios.py
Imprimir chaves, valores e chaves com os valores

funcoes.py
Funções aritméticas e uso do LAMBDA

exemplos.py
Utilização dos values e dos items de tuplas

list_comprehension.py
Criaçaõ de listas. Filtragem de elementos das listas. Desempacotamento de listas. Mapeamento de Listas

Pessoas
pessoas.py
Construtor da classe Pessoa
gravar_dados.py
Utilização da classe Pessoa para inserir dados, transformar em dicionário e criar um .json com os dados criados
ler_dados.py
Lê os dados do ficheiro .json criado no gravar_dados



FICHAS

Ficha1

1. Crie uma função em Python que receba um número qualquer de argumentos e
devolva a soma dos valores que estejam entre 5 e 10.

2. Crie uma função anónima em Python que necessite de um argumento. A função
retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu
argumento for zero ou negativo.

3. Crie uma função em Python que retorne o reverso de um número inteiro dado
pelo utilizador. Por exemplo: 127 -> 721.

4. Crie uma função anónima que informe a quantidade de dígitos de um
determinado número inteiro dado pelo utilizador.

5. Um número é dito perfeito quando ele é igual a soma de seus fatores. Considere
o seguinte exemplo: os fatores de 6 são 1, 2 e 3 (ou seja, podemos dividir 6 por
1, por 2 e por 3) e 6=1+2+3, logo 6 é um número perfeito. Crie uma função que
recebe um inteiro e que no final indique se o número indicado é perfeito ou
não.

Ficha2

1. Através da utilização da função map, crie códigos que devolvam os resultados
pretendidos:

a. Devolva uma lista de 0’s e 1’s conforme o sexo seja M (1) ou F (0).

b. Devolva uma lista de tuplas com o nome da pessoa e 0’s ou 1’s conforme
o sexo da pessoa.

c. Devolva uma tupla de tuplas com o nome e o IMC da pessoa. IMC =
peso/(altura*altura).

2. Crie uma função que devolva uma tupla com a média do peso e da altura de
todas as pessoas.

Ficha3


1. Crie uma lista com os números pares de 1 a 10.

2. Crie uma lista com os quadrados dos números de 1 a 10.

3. Dada uma lista de palavras, crie uma nova lista que indique o tamanho de cada
palavra.

4. Dada uma lista de números, crie uma lista apenas com os números maiores que 5.

5. Crie uma lista com as letras maiúsculas de uma string. (nome = 'MarcelO ViEiRa
amorIM')

6. Dada uma lista de números, crie uma nova lista onde se o número for múltiplo de 3,
é apresentado o dobro deste caso contrário aparece o mesmo número da lista original.

7. Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam
com a letra "A". Todos os nomes da nova lista devem aparecer em maiúsculas.

8. Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta,
apenas para as frutas com mais de 5 letras. Caso contrário, deve aparecer 0.

Ficha4

1. Crie um ficheiro .py no Visual Studio Code denominado main.py (deve ser criada uma
nova pasta denominada Produtos que deve ser a raiz da aplicação).

2. Crie uma lista vazia denominada products.

3. Crie uma função que receba o nome do produto, o preço e o iva e guarde a informação
em um dicionário onde as chaves serão product, price e tax. A função deve ser
denominada add.

4. Crie uma função a partir da lista anterior que inclua no dicionário anterior uma nova
chave ‘final_price’ que calcule o seu preço final (price * (1+tax)).
▪ O preço final deve ser apresentado com duas casas decimais.
▪ O nome da função deverá ser update_final_price.

5. Teste as funções criadas nas alíneas 3 e 4.

6. Crie uma função que imprima no ecrã os dados de um produto específico (produto,
price, tax e final_price). A função deve receber o nome de print_product().

7. Teste a função da alínea anterior imprimindo no ecrã todos os produtos inseridos até
ao momento.

Ficha5

▪ Cada classe deverá ficar em ficheiro separado.

▪ Classe Triangulo

o Precisam de 3 lados para serem definidos.

o Deve ser possível testar se é possível formar um triângulo com os lados
dados. Se um lado for maior que a soma dos outros dois, não é possível
formar um triângulo.

o Calcular o perímetro do triângulo (soma dos 3 lados)

o Calcular a área de um triângulo.

▪ p é o semiperímetro do triângulo

o Saber se o triângulo é equilátero (3 lados iguais), isósceles (2 lados iguais)
ou escaleno.

▪ Classe Retangulo

o Deve permitir definir os lados de um retangulo e uma cor.

o Deve ser possível saber se o retangulo é um quadrado.

o Deve ser possível determinar a diagonal do retângulo. (Raiz quadrada
da soma do quadrado de cada lado)

o Deve ser possível saber se os dois retângulos possuem o mesmo
perímetro.

o Deve ser possível saber se os dois retângulos possuem a mesma cor.


▪ Classe ComandoTv

o O comando deve possuir as seguintes informações:
▪ Marca
▪ Ano de fabrico
▪ Canal
▪ Volume
▪ Ligado ou desligado

o Deve ser possível trocar de canal. Só deve aceitar canais entre 1 e 99.
Qualquer outro valor deve emitir um aviso e ficar no canal atual.

o Deve ser possível aumentar/diminuir o volume. Deve possuir um
parâmetro que indica se é para aumentar ou diminuir o volume. O valor
mínimo do volume é 0 e o valor máximo 50.

o Um método para colocar o volume a zero.

o Um método para ligar/desligar o comando. Deve aparecer uma
mensagem a indicar quando o comando está ligado ou desligado.

o Um método que mostre os dados do comando: marca, ano, canal atual,
volume atual.

▪ Após a criação das três classes, estas devem ser testadas em um ficheiro criado
para o efeito.