# Faça um programa que permite selecionar e jogar os seguintes jogos (use funções):
# (a) Jogo do galo;
# (b) Jogo 4 em linha;
# (c) Jogo da gloria (ex. https://bit.ly/2Ucrusu; https://bit.ly/3xBwi8j;
# https://bit.ly/3xxsjcU)
from Aula_4 import EX4, EX5


def MostrarMenu():
    print("-=-=--=-=--=-=--=-=--=-=--=-=-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-")
    print("-=-=--=-=--=-=--=-=--=-=--=-=-=-=-=-MENU-=-=--=-=--=-=--=-=--=-=--=-=--=-=-=-=-")
    print("-=-=--=-=--=-=--=-=--=-=--=-(1) Jogo Do Galo")
    print("-=-=--=-=--=-=--=-=--=-=--=-(2) Jogo 4 em linha")
    print("-=-=--=-=--=-=--=-=--=-=--=-(3) Jogo da gloria")
    print("-=-=--=-=--=-=--=-=--=-=--=-=-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-")


MostrarMenu()
opcao = int(input("Qual jogo você deseja jogar? "))
if opcao == 0:
    print(" ")
if opcao == 1:
    EX4()
if opcao == 2:
    EX5()
