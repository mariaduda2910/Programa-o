# Implemente um programa para calcular a somatório dos números existentes num
# intervalo definido por limites inferior e superior.
inferior = 1
superior = 5
soma = 0
if inferior <= superior:
    for i in range(inferior, superior + 1):
        soma = soma + i
        i = i + 1
print(soma)
