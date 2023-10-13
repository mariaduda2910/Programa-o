# implemente um programa para determinar nome e idade da pessoa mais nova de um
# grupo. Ler o número do Cartão de Cidadão e a idade de uma série de pessoas, e o
# programa deve terminar quando for introduzido a idade da pessoa = 999. No final deve
# ser mostrado o nome e idade da pessoa mais nova
idade = 0
nome = 0
cartao_cd = 0
menor_idade = 998
nome_da_menor = 0
numero_cc_menor = 0
while idade != 999:
    idade = int(input("Qual sua idade?"))
    if idade == 999:
        break
    nome = input("Qual seu nome?")
    cartao_cd = int(input("Qual o número do seu CC?"))
    if idade < menor_idade:
        menor_idade = idade
        nome_da_menor = nome
        numero_cc_menor = cartao_cd
    elif idade == menor_idade:
        menor_idade = idade
        nome_da_menor = nome
        numero_cc_menor = cartao_cd
if idade == 999:
    print("A pessoa mais nova tem",menor_idade,"anos. Seu nome é", nome_da_menor)
