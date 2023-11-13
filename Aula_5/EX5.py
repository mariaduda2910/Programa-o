# Implemente um programa que tenha uma função para ordenar um vetor, retornando
# esse vetor ordenado
def OrdenarVetor(vetor):
    x = sorted(vetor)
    return x

vetor = [5, 2, 9, 1, 6]
vetor_ordenado = OrdenarVetor(vetor)

print("Vetor:", vetor)
print("Vetor ordenado:", vetor_ordenado)
