# Escreva o algoritmo e o programa para calcular a fórmula resolvente de equações de 2º
# grau,
# Os valores a, b, e c, devem ser gerados aleatoriamente. O valor de a varia entre [0, 10],
# e os valores b e c variam entre [5, 20]. Se (b^2 - 4ac) < 0, o output deve ser “não
# existem raízes reais”.
import random

# import random

a = random.randint(1, 10)
b = random.randint(5, 20)
c = random.randint(5, 20)

d = (b ** 2) - 4 * a * c

if d < 0:
    print("não existem raízes reais")
else:
    s1 = (-b + d ** 0.5) / 2 * a
    s2 = (-b - d ** 0.5) / 2 * a
