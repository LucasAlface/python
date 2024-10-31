class ComandoTv:
    def __init__(self,marca,ano_fabrico,canal):
        self.marca = marca
        self.ano_fabrico = ano_fabrico
        self.canal = canal
        self.volume = 0
        self.ligado = False

    # Função para mudar o canal do comando
    def mudarCanal(self,novo_canal):
        if novo_canal < 1 or novo_canal > 100: # Filtrar para permitir apenas valores entre 1 e 100
            novo_canal = self.canal # Caso seja menor que 1 ou maior que 100, o canal mantêm-se
            print('Canal invalido')
        return novo_canal
    
    # Alterar volume do comando de 1 em 1
    def alterarVolume(self,sinal):
        if self.volume > 0 and sinal == '-':
            self.volume -= 1
        if self.volume < 50 and sinal == '+':
            self.volume += 1

    # Meter volume a 0
    def mute(self):
        self.volume = 0

    # Ligar/Desliagr
    def on_off(self):
        if self.ligado == True:
            self.ligado = False
            print('Comando desligado')
        else:
            self.ligado = True
            print('Comando ligado')

    def dadosAtuais(self):
        return f'Marca: {self.marca} \n Ano fabricacao: {self.ano_fabrico} \n Canal: {self.Canal} \n Volume: {self.volume} \n Estado: {self.ligado}'

c1 = ComandoTv('Sigma', 1999, 30)

c1.alterarVolume('-')

print(c1.volume)

print(c1.dadosAtuais)

        