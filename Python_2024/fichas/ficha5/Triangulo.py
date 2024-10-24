from math import sqrt # importar raiz quadrada

class Triangulo:
    # Cosntrutor
    def __init__(self,Lado1=0,Lado2=0,Lado3=0):
        self.lado1 = Lado1
        self.lado2 = Lado2
        self.lado3 = Lado3
    
    # Verifica se é um triângulo
    def isTriangle(self):
        # Se um lado for maior que os outros 2 juntos, não pode ser um triângulo
        return self.lado1 < self.lado2 + self.lado3 and self.lado2 < self.lado1 + self.lado3 and self.lado3 < self.lado1 + self.lado2 
    
    # Calcular perimetro
    def perimetro(self):
        if self.isTriangle():
            return self.lado1 + self.lado2 + self.lado3
        else:
            return "Nao e possivel formar um triangulo"

    # Calcular area do triangulo
    def area(self):
        if self.isTriangle():
            sp = self.perimetro() / 2
            return round(sqrt(sp*(sp-self.lado1)*(sp-self.lado2)*(sp-self.lado3)),2)
        else:
            return "Nao e possivel formar um triangulo"

    # Saber qual o tipo do triangulo
    def tipoTriangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilatero"
        elif self.lado1 != self.lado2 and self.lado2 != self.lado3 and self.lado1 != self.lado3:
            return "Escaleno"
        return "Isosceles" # Se não for Equilatero ou Escaleno, tem de ser Isosceles


tr1 = Triangulo(9,11,20)
tr2 = Triangulo(2,2,3)
