# Exercício
# Faça o algoritmo e implemente o programa do Jogo da forca
# (https://pt.wikipedia.org/wiki/Jogo_da_forca)
import random
def JogoDaForca():
    def MostrarBoneco(count):
        if count == 1:
            print("____________\n"
                  "|          |\n"
                  "|          O\n"
                  "|\n"
                  "|\n"
                  "|")
        elif count == 2:
            print("____________\n"
                  "|          |\n"
                  "|          O\n"
                  "|          |\n"
                  "|\n"
                  "|"
                  )
        elif count == 3:
            print("____________\n"
                  "|          |\n"
                  "|          O\n"
                  "|         /|\n"
                  "|\n"
                  "|"
                  )
        elif count == 4:
            print("____________\n"
                  "|          |\n"
                  "|          O\n"
                  "|         /|\.\n"
                  "|\n"
                  "|"
                  )
        elif count == 5:
            print("____________\n"
                  "|          |\n"
                  "|          O\n"
                  "|         /|\.\n"
                  "|         / \n"
                  "|"
                  )
        elif count == 6:
            print("____________\n"
                  "|          |\n"
                  "|          O\n"
                  "|         /|\.\n"
                  "|         / \.\n"
                  "|"
                  )
        elif count == 7:
            print("____________\n"
                  "|          |\n"
                  "|          O\n"
                  "|  ----------------\n"
                  "|         /|\.\n"
                  "|         / \.\n"
                  "|"
                  )

    def PalavraSecreta(palavra):
        caracteres = (len(palavra))
        palavra_secreta = ["_"] * caracteres
        return palavra_secreta

    def ConfirmarLetra(letra, palavra):
        indices = []
        for i in range(len(palavra)):
            if palavra[i] == letra:
                indices.append(i)
        return indices


    lista_ordenada = []
    lista_de_letras = []
    count = 0
    listaDeElementos = ["FACA", "GARFO", "ABAJUR", "LUZ"]

    ##Qual é a palavra ##
    palavra = random.choice(listaDeElementos)
    palavra_secreta = PalavraSecreta(palavra)
    letraCerta = 0
    print(palavra_secreta)

    # Começa a jogar o jogo
    while True:
        letra = input("Qual é a letra? ").upper()
        if letra not in lista_de_letras:
            lista_de_letras.append(letra)
            lista_ordenada = sorted(lista_de_letras)
            print("letras ja utilizada: {}".format(lista_ordenada))
            if letra in palavra:
                indice = ConfirmarLetra(letra, palavra)
                for i in range(len(indice)):
                    palavra_secreta[indice[i]] = letra
                    letraCerta = letraCerta + 1
                print(palavra_secreta)
                if len(palavra_secreta) == letraCerta:
                    print("Parabens!! Você ganhou!!!")
                    break
            else:
                count += 1
                MostrarBoneco(count)
                if count == 7:
                    print("Sinto muito vc perdeu!!! A palavra secreta era {}".format(palavra))
                    break
        else:
            print("Essa letra ja foi utilizada, veja a seguir a lista de letras que já foram utilizadas{}".format(lista_ordenada))


if __name__ == "__main__":
    JogoDaForca()
