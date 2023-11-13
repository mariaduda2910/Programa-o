# Implemente um programa que tenha uma função para procurar um número num vetor,
# retornando “true” caso detete o número, “false” caso contrário.
lista = [1, 52, 47, 54]


def procurarUmNumero(lista,objeto):
    if objeto in lista:
        return True
    else:
        return False


objeto = int(input("Qual é o objeto que deseja procurar?"))
if procurarUmNumero(lista, objeto):
    print("encontra-se na lista")
else:
    print("nao se encontra na lista")
