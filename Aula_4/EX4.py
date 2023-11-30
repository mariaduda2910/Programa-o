""" Implemente o algoritmo e implemente o programa do jogo galo (jogo da velha ou três
# em linha)"""
import math
def JogoDaVelha():
    itens = ["X", "O"]
    tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ganhador = 0
    empate = 0
    print("_=_=_=_=_=_=_=_\n | {0} | {1} | {2} |\n | {3} | {4} | {5} |\n | {6} | {7} | {8} |\n_=_=_=_=_=_=_=_".format(
        tabuleiro[0],
        (tabuleiro[1]),
        (tabuleiro[2]),
        (tabuleiro[3]),
        (tabuleiro[4]),
        (tabuleiro[5]),
        (tabuleiro[6]),
        (tabuleiro[7]),
        (tabuleiro[8])))
    for jogadas in range(1, 10):
        if jogadas % 2 != 0:
            while True:
                jogador_X = int(input("Jogador X, qual será sua jogada?"))
                if tabuleiro[jogador_X] == "X" or tabuleiro[jogador_X] == "O":
                    print("Essa posição encontra-se ocupada. Tente outra posição. ")
                else:
                    break

            tabuleiro[jogador_X] = itens[0]
            print(
                "-----------------\n | {0} | {1} | {2} |\n | {3} | {4} | {5} |\n | {6} | {7} | {8} |\n".format(tabuleiro[0],
                                                                                                               (tabuleiro[
                                                                                                                   1]),
                                                                                                               (tabuleiro[
                                                                                                                   2]),
                                                                                                               (tabuleiro[
                                                                                                                   3]),
                                                                                                               (tabuleiro[
                                                                                                                   4]),
                                                                                                               (tabuleiro[
                                                                                                                   5]),
                                                                                                               (tabuleiro[
                                                                                                                   6]),
                                                                                                               (tabuleiro[
                                                                                                                   7]),
                                                                                                               (tabuleiro[
                                                                                                                   8])))
            ganhador = itens[0]
            if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
        else:
            while True:
                jogador_O = int(input("Jogador O, qual será sua jogada??"))
                if tabuleiro[jogador_O] == "X" or tabuleiro[jogador_O] == "O":
                    print("Essa posição encontra-se ocupada. Tente outra posição. ")
                else:
                    break
            tabuleiro[jogador_O] = itens[1]
            print(
                "_=_=_=_=_=_=_=_\n | {0} | {1} | {2} |\n | {3} | {4} | {5} |\n | {6} | {7} | {8} |\n_=_=_=_=_=_=_=_".format(
                    tabuleiro[0],
                    (tabuleiro[1]),
                    (tabuleiro[2]),
                    (tabuleiro[3]),
                    (tabuleiro[4]),
                    (tabuleiro[5]),
                    (tabuleiro[6]),
                    (tabuleiro[7]),
                    (tabuleiro[8])))
            ganhador = itens[1]
            if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break
            if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
                print("Você ganhou!!! Jogador {}".format(ganhador))
                break


        print(jogadas)
    if jogadas >= 9:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
              "\nParabéns aos jogadores, o jogo foi empatado!!!Talvez na próxima tentativa\n"
              "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

if __name__ == "__main__":
    JogoDaVelha()