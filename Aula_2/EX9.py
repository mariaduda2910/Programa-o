# # Implemente um programa para calcular:
# # (a) a média das idades e das alturas de todos os alunos da turma;
# # (b) qual a altura do aluno mais alto
# # (c) qual a idade do aluno mais novo
# idades_dos_alunos = []
# altura_dos_alunos = []
# alunos = int(input("Quantos alunos serão inseridos?"))
# for i in range(alunos):
#     idades = int(input("Qual é a sua idade?"))
#     altura = float(input("Qual é a sua altura?"))
#     idades_dos_alunos.append(idades)
# print(sum(idades_dos_alunos))
# print(sum(altura_dos_alunos))
#
# print("O aluno mais velho tem",max(idades_dos_alunos), "anos.")
# print("O aluno mais alto tem",max(idades_dos_alunos), "metros.")
alunos = int(input("quantos alunos tem na turma?"))
idade = 0
altura = 0
idade_menor = 100
altura_maior = 0
soma_2 = 0
soma_1 = 0
i = 0
while i < alunos:
    idade = int(input("Qual a idade?"))
    if idade <= idade_menor:
        idade_menor = idade
    altura = float(input("Qual a altura?"))
    if  altura >= altura_maior:
        altura_maior = altura
    soma_idade = idade
    soma_1 = soma_idade + idade
    soma_altura = altura
    soma_2 = soma_altura + altura
    i += 1
print("A altura do maior é", altura_maior,"metros")
print("A idade do menor é", idade_menor,"anos")
print("A média das alturas é",soma_2/alunos,"A média das idades é", soma_1/alunos)

