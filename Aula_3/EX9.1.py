# Escreva o algoritmo e o programa para todos os estudantes do TeSP do ISE-DEE por
# turma, ler (não use vetores e/ou matrizes e/ou strings):
# (a) a idade;
# (b) o género (masculino – 1; feminino – 0);
# (c) nota de entrada.
# Apresente:
# (i) qual a turma com o aluno mais novo
# (ii) qual a turma com o aluno mais velho
# (iii) quantas raparigas existem nos TeSP-DEE
# (iv) qual a turma com o aluno com a nota de entrada mais alta
# (v) qual a nota de entrada mais alta e o género da pessoa que teve essa nota
# turmas = int(input("O aluno está na turma 1 ou 2?"))

turma = 0
idade = 0
genero = 0
nota = 0
nota_alta = 0
idade_menor = 100
idade_maior = 0
meninas = 0
turma_maior_nota = 0
genero_nota_alta = 0
turma_menor = 0
turma_maior = 0

alunos = int(input("Quantos alunos serão inseridos?"))
for i in range(alunos):
    turma = int(input("Qual turma o aluno pertence:"))
    idade = int(input(" Idade do aluno:"))
    if idade <= idade_menor:
        idade_menor = idade
        turma_menor = turma
    if idade >= idade_maior:
        idade_maior = idade
        turma_maior = turma
    genero = int(input(" Marque genero: masculino – 1; feminino – 0:"))
    nota = float(input("Nota de entrada do aluno:"))
    if nota > nota_alta:
        nota_alta = nota
        turma_maior_nota = turma
        print("A nota mais alta é", nota_alta)
        if genero == 0:
            genero_nota_alta = "feminino"
        elif genero == 1:
            genero_nota_alta = "masculino"
    if genero == 0:
        meninas = meninas + 1
print("A turma com o aluno mais novo é", turma_menor, "A turma com o aluno mais velho é", turma_maior)
print("Existem {} meninas na tesp".format(meninas))
print("O aluno com a nota mais alta pertence a turma {0}, sua nota foi {1}, e seu genero é {2}".format(turma_maior_nota,
                                                                                                       nota_alta,
                                                                                                       genero_nota_alta))
