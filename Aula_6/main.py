# Faça um programa que permite selecionar e jogar os seguintes jogos (use funções):
# (a) Jogo do galo;
# (b) Jogo 4 em linha;
# (c) Jogo da gloria (ex. https://bit.ly/2Ucrusu; https://bit.ly/3xBwi8j;
# https://bit.ly/3xxsjcU)
import sys
sys.path.insert()
from Aula_4 import *
def mostrar_menu():
    print("-=-=--=-=--=-=--=-=--=-=--=-=-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-")
    print("-=-=--=-=--=-=--=-=--=-=--=-=-=-=-=-MENU-=-=--=-=--=-=--=-=--=-=--=-=--=-=-=-=-")
    print("(1) Jogo Do Galo")
    print("(2) Jogo 4 em linha")
    print("(3) Jogo da gloria")

def menu():

    mostrar_menu()
    opcao = input("Qual jogo você deseja jogar? ")
    if opcao == 1:
        Aula_4.EX4()
        # case 2 :
        # case 3 :

menu()

