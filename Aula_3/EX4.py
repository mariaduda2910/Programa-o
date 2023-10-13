# Implemente um programa para fazer a tabuada de um número lido.
numero = float(input("Insira um número inteiro: "))
if numero >= 1:
    for i in range(11):
        tabuada = numero * i
        print(i, "x", numero, "=", tabuada)
