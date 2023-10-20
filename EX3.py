#Faça o algoritmo: Leia as notas de um aluno às disciplinas de Matemática, Português,
#Inglês e Geografia e calcule a média. Em função da média mostra uma mensagem com
#o conteúdo "Aprovado" ou "Reprovado". Consideram-se notas positivas as notas iguais
#ou superiores a 9,5.

mat = float(input("Qual a nota em mat?"))
port = float(input("Qual a nota em port?"))
ing = float(input("Qual a nota em ing?"))
geo = float(input("Qual a nota em geo?"))
media = (mat + port + ing + geo)/4
if media >= 9.5:
    print("Aprovado")
else:
    print("Reprovado")

