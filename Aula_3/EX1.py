# Implemente um programa para determinar se um número é primo (um número é primo
# se for apenas divisível por si próprio e pela unidade).
numero = int(input("Insira um número inteiro para confirmar se é primo. "))
if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(" Não é um número primo")
            break
    else:
        print(numero, "é primo")
else:
    print("Não é um número primo")


