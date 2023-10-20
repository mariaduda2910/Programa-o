#Faça o algoritmo: Calcular o fatorial de um número, i.e.,
numero = int(input("Qual o número?"))
contador = 1
fatorial = 1
while contador <= numero:
    fatorial *= contador
    contador += 1
    print(contador)
print(fatorial)