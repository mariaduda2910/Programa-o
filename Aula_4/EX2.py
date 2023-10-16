# Implemente um programa que ordene uma lista de N elementos
lista = []
numeros = int(input("Quantos números serão introduzidos?"))
for i in range(numeros):
    lista.append(input("insira o valor: "))
    print(sorted(lista))
