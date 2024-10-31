from math import sqrt, pow

class Retangulo:
    def __init__(self, largura, altura, cor):
        self.largura = largura
        self.altura = altura
        self.cor = cor

    # Verfica se o retângulo é quadrado
    def isSquare(self):
        return self.altura == self.largura # Verifica se a condição é verdadeira e retorna de acordo com o resultado
    
    # Calcula a diagonal do retangulo
    def diagonal(self):
        return sqrt(pow(self.altura,2) + pow(self.largura,2))
    
    # Calcula o perimetro
    def perimetro(self):
        return 2*self.altura + 2*self.largura
    
    # Verfica se 2 retângulos têm o mesmo perímetro
    def mesmoPerimetro(self,r):
        return self.perimetro() == r.perimetro()
    
    # Verfica se 2 retângulos têm a mesma cor
    def mesmaCor(self,r):
        return self.cor == r.cor
    
r1 = Retangulo(8,12,'Azul')
r2 = Retangulo(8,12,'Vermelho')
