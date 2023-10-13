# Implemente um programa para calcular a área e verifica se é um quadrado ou um
# retângulo.
base = float(input("Qual o valor da base?"))
altura = float(input("Qual o valor da altura?"))
area = base * altura
if area == 0:
    print("o valor em um dos campos não pode ser 0")
elif base == altura:
    print("é um quadrado")
else:
    print("é um retangulo")