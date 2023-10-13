# Implemente um programa para determinar o máximo de 3 valores. Ex. 123, 23 e 4 ->
# retorna máximo é “123”.
n1 = float(input("insira o 1 valor:"))
n2 = float(input("insira o 2 valor:"))
n3 = float(input("insira o 3 valor:"))
if n1 > n2 and n1 > n3:
    print("%d é o maior" % n1)
elif n2 > n3:
    print("%d é o maior" % n2)
else:
    print("%d é o maior" % n3)
--------------------------------------------------------------
numero = []
for i in range(3):
    numero.append(float(input("Digite 1 numero:")))
    print(numero)
print(max(numero))
print(min(numero))