# Implemente um programa que tenha uma função que leia o nome do utilizador (ex. João
# Miguel Rodrigues) e coloque o apelido em primeiro lugar seguida de uma virgula (ex.
# Rodrigues, João Miguel)
def LerNome(nome):
    nome_completo = nome.split()
    print(nome_completo)
    print(nome_completo[-1], ",", nome_completo[0])
nome = input("Qual seu nome completo?")
LerNome(nome)
