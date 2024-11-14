from Classes import Aluno
from Ler_Gravar_Dados import salvar_alunos, carregar_alunos

a1 = Aluno("Lucas Soares", 16, "a14581@oficina.pt", "943745923", "Programador de Infomática")
a2 = Aluno("Michel Andrade", 18, "a15432@oficina.pt", "973426712", "Multimédia")
a3 = Aluno("Luís Santos", 43, "luissantos@oficina.pt", "934823745", "Audiovisuais")

alunos = [a1, a2, a3] # Cria uma lista para poder ser enviada para a função

salvar_alunos(alunos)

alunos_carregados = carregar_alunos()

# Imprimir os alunos carregados
for aluno in alunos_carregados:
    print(f'\n{aluno}')