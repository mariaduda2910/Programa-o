# Implemente um programa que tenha uma função que leia o nome do utilizador (ex. João
# Miguel Rodrigues) e coloque o apelido em primeiro lugar seguida de uma virgula (ex.
# Rodrigues, João Miguel)
def InverterNome(nome):
    nome_completo = nome.split()
    nome_temp = nome_completo[-1] + ", "
    for elemento in nome_completo[:-1]:
        nome_temp += elemento + " "
    return nome_temp

nome = input("Qual seu nome completo?")
nome_invertido = InverterNome(nome)
print(nome_invertido)