# Exercício 1
# Implemente um programa que permita a leitura de 10 valores (inteiros), guardando-os
# numa lista, imprima a diferença entre o maior e o menor valor do vetor, bem como o
# número de valores pares e ímpares do vetor.
lista = []
numero = 0
pares = 0
impares = 0
for numero in range(10):
    lista.append(float(input("insira o valor: ")))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print(max(lista) - min(lista))
print("Possui {0} numeros impares e {1} numeros pares".format(impares,pares))
