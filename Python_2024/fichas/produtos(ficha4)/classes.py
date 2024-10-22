class ContaBancaria:
    #Construtor
    def __init__(self,cliente,saldo,agencia):
        self.cliente = cliente
        self.saldo_inicial = saldo
        self.agencia = agencia
        self.emprestimo = False

    def depositar(self,valor):
        self.saldo_inicial = self.saldo_inicial + valor

    def levantar(self,valor):
        if self.saldo_inicial > valor:
            self.saldo_inicial = self.saldo_inicial - valor
        else:
            print('Saldo insuficiente')

c1 = ContaBancaria('Lucas', 1000.00, 'Rebordoes')
c2 = ContaBancaria('Filipe', 500.0, 'Ribeirao')
c2.depositar(200)
print(c2.saldo_inicial)
