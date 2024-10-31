class A:
    atributo_a = 'Valor de a'

    def __init__(self,atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'Valor de b'

    def __init__(self,atributo,outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
