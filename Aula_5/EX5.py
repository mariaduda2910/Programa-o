# Implemente um programa que tenha uma função para ordenar um vetor, retornando
# esse vetor ordenado
def Ordenar_Vetor(vetor):
    x = sorted(vetor)
    return x

vetor = [5, 2, 9, 1, 6]
vetor_ordenado = Ordenar_Vetor(vetor)

print("Vetor original:", vetor)
print("Vetor ordenado:", vetor_ordenado)
