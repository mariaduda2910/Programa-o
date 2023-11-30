# Faça um programa que permite selecionar e jogar os seguintes jogos (use funções):
# (a) Jogo do galo;
# (b) Jogo 4 em linha;
# (c) Jogo da gloria (ex. https://bit.ly/2Ucrusu; https://bit.ly/3xBwi8j;
# https://bit.ly/3xxsjcU)
from Aula_4.EX4 import JogoDaVelha
from Aula_4.EX5 import JogoQuatroEmLinhas
from Aula_7_8.EX1 import JogoDaForca
from time import sleep


# from Aula_6.Jogo_da_gloria import Jogodagloria
def MostrarMenu():
    print("-=-=--=-=--=-=--=-=--=-=--=-=-=-=-=-MENU-=-=--=-=--=-=--=-=--=-=--=-=--=-=-=-=-")
    print("| (1) Jogo Do Galo                                                              |")
    print("| (2) Jogo 4 em linha                                                           |")
    print("| (3) Jogo da gloria                                                            |")
    print("| (4) Jogo da Forca                                                             |")
    print("| (0) Sair                                                                      |")
    print("-=-=--=-=--=-=--=-=--=-=--=-=-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-")


def EscolheMenu():
    MostrarMenu()
    while True:
        try:
            print(".........loading")
            sleep(2)
            opcao = int(input(
            "Esse é nosso MENU interativo! \n Pressione o número do jogo desejado e divirta-se jogando cada um deles: "))
            if opcao == 0:
                print("........zZZ")
                sleep(1)
                print("Tchau jogador. Até a próxima !!!")
                break
            if opcao == 1:
                print("Ihulll Vamos jogar o jogo da velha!!!!")
                sleep(1)
                JogoDaVelha()
                break
            if opcao == 2:
                print("Ihulll Vamos jogar o Jogo Quatro em linhas!!!!")
                sleep(1)
                JogoQuatroEmLinhas()
                break
            if opcao == 3:
                print("Ihulll Vamos jogar o.......!!!!")
                sleep(1)
                print("Ops, ainda n esta feito ")
            if opcao == 4:
                print("Ihulll Vamos jogar o Jogo da Forca!!!!")
                sleep(1)
                JogoDaForca()
            else:
                print("OPS...... Essa opção não é válida, pfv tente novamente com uma das opções válidas.")
        except ValueError:
            print("OPS...... Essa opção não é válida, pfv tente novamente com uma das opções válidas.")

EscolheMenu()
