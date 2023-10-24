# Implemente um programa que tenha uma função para procurar um número num vetor,
# retornando “true” caso detete o número, “false” caso contrário.
lista = [1,52,47,54]
def TrueFalse(lista):
    objeto = input("Qual é o objeto que deseja procurar?")
    if lista.index(objeto) == True:
        return True
    else:
        return False
TrueFalse(lista)