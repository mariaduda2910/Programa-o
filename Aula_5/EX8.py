# Implemente um programa que tenha funções que leiam o nome das disciplinas (UC) do
# presente semestre e a nota esperada para cada uma. Retire as iniciais (sigla) e de cada
# UC (ex. Programação – P; Programação Orientada Objetos – POO), e que coloque no
# ecrã a sigla – nota
def NotaDisciplina(disciplina,nota):
    dividir = disciplina.split()
    letras_removidas = [i[0] for i in dividir]
    sigla = ''.join(letras_removidas).upper()
    notas = nota
    return sigla, notas

nome_das_disciplinas = input("Disciplina: ")
nota = int(input("Nota desejada: "))
letras_removidas = NotaDisciplina(nome_das_disciplinas,nota)

print(letras_removidas)
