# Exercício
# Faça o algoritmo e implemente o programa do Jogo da forca
# (https://pt.wikipedia.org/wiki/Jogo_da_forca)
def MostrarBoneco(count):
    if count == 1:
        cabeca = " O"
        print(cabeca)
    elif count == 2:
        corpo = "  O\n I"
        print(corpo)
    elif count == 3:
        print("  O\n /I")
    elif count == 4:
        print("  O\n /I|")
    elif count == 4:
        print("  O\n /I|\n  |")
    elif count == 5:
        print("  O\n /I|\n ||")
    elif count == 6:
        print("morreu")


def PalavraSecreta(palavra):
    caracteres = (len(palavra))
    palavra_secreta = [" * "] * caracteres
    return palavra_secreta

def ConfirmarLetra(palavra, letra):
    try:
        index_da_letra = palavra.index(letra)
        return palavra[index_da_letra]
    except ValueError:
        print("ops letra errada")
        return False

count = 0
palavra = input("Qual é a palavra secreta ?").upper()
lista_palavra = list(palavra)
print(PalavraSecreta(lista_palavra))
# Começa a jogar o jogo
while True:
    letra = input("Qual é a letra? ").upper()
    print(ConfirmarLetra(lista_palavra,letra))
    if ConfirmarLetra(lista_palavra,letra) == False:
        count = + 1
        MostrarBoneco(count)
