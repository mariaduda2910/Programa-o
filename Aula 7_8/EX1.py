# Exercício
# Faça o algoritmo e implemente o programa do Jogo da forca
# (https://pt.wikipedia.org/wiki/Jogo_da_forca)
def MostrarBoneco(count):
    if count == 1:
        cabeca = " O"
        print(cabeca)
    elif count == 2:
        corpo = "  O\n  I"
        print(corpo)
    elif count == 3:
        print("  O\n /I")
    elif count == 4:
        print("  O\n /I|")
    elif count == 5:
        print("  O\n /I|\n  |")
    elif count == 6:
        print("  O\n /I|\n ||")
    elif count == 7:
        print("morreu")


def PalavraSecreta(palavra):
    caracteres = (len(palavra))
    palavra_secreta = [" * "] * caracteres
    return palavra_secreta


def ConfirmarLetra(palavra, letra):
    if letra in palavra:
        return True
    else:
        return False


lista_ordenada = []
lista_de_letras = []
count = 0

##Qual é a palavra ##
palavra = input("Qual é a palavra secreta ?").upper()
lista_palavra = list(palavra)
palavra_secreta = PalavraSecreta(lista_palavra)
print(palavra_secreta)

# Começa a jogar o jogo
while True:
    letra = input("Qual é a letra? ").upper()
    if letra not in lista_de_letras:
        lista_de_letras.append(letra)
        lista_ordenada = sorted(lista_de_letras)
        print("letras ja utilizada: {}".format(lista_ordenada))
        if ConfirmarLetra(lista_palavra, letra):
            print(lista_palavra.count(letra))
            index_da_letra = lista_palavra.index(letra)
            palavra_secreta[index_da_letra] = letra
            print(palavra_secreta)
        else:
            count = count + 1
            MostrarBoneco(count)
            if count == 7:
                break
    else:
        print("Essa letra ja foi utilizada, veja a seguir a lista de letras que já foram utilizadas{}".format(
            lista_ordenada))

print("Sinto muito vc perdeu!!! A palavra secreta era {}".format(palavra))
