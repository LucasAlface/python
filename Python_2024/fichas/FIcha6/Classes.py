class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    # Método para sobrepor o __str__ e devolver a informação tratada
    def __str__(self):
        return f'Nome: {self.nome} \nIdade: {self.idade} \nEmail: {self.email}'
    

class Aluno(Pessoa):
    def __init__(self, nome, idade, email, matricula, curso):
        super().__init__(nome, idade, email) # Herança da classe pai
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        return f'{super().__str__()} \nMatrícula: {self.matricula} \nCurso: {self.curso}' # Pega no método da classe pai e adiciona os atributos da própria classe