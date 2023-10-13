# Implemente um programa para determinar perímetro e área de circunferência.
#area
pi = 3.14
raio = float(input("digite o valor do raio="))
area = pi * (raio**2)
print("Valor da area é {}".format(area))

# perimetro
perimetro = 2 * pi * raio
print("Valor do perimetro confere a {} ".format(perimetro))