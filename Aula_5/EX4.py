# Implemente um programa que permita: a) Uma função que faça a leitura de 10 valores
# (inteiros), guardando-os num vetor; b) Uma função que retorne a diferença entre o
# maior e o menor valor do vetor; c) Uma função que devolva o número de valores pares
# e ímpares do vetor.
def ValoresInteiros():
    lista = []
    for i in range(10):
        lista.append(int(input("Insira valores: ")))
    return lista


def Subtrair():
    maximo = max(valores)
    minimo = min(valores)
    return maximo - minimo


def ParesImpares(valores):
    pares = []
    impares = []
    for valores in valores:
        if valores % 2 == 0:
            pares.append(valores)
        else:
            impares.append(valores)
    return len(pares), len(impares)


valores = ValoresInteiros()
print("A subtração do maior valor pelo menor da seguinte lista", valores, "é igual a ", Subtrair(valores))
pares, impares = ParesImpares(valores)
print("São ", pares, " pares", "e", impares, " impares")
