# Implemente um programa para calcular o fatorial de um número
numero = int(input("insira um número inteiro: "))
fatorial = 1
if numero < 0:
    print("Não existe fatorial de números negativos")
elif numero > 0:
    for i in range(1, numero + 1):
        fatorial = fatorial * i
        print(fatorial)

else:
    print("1")
