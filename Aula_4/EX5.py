def JogoQuatroEmLinhas():
    itens = ["X", "O"]
    tabuleiro = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "]]

    def mostrar_tabuleiro(tabuleiro):
        print("_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=\n |0  |1  |2  |3  |4  |5  |6  |")

        for i in range(0, 6):
            print(" | {0} | {1} | {2} | {3} | {4} | {5} | {6} |".format((tabuleiro[0][i]),
                                                                        (tabuleiro[1][i]),
                                                                        (tabuleiro[2][i]),
                                                                        (tabuleiro[3][i]),
                                                                        (tabuleiro[4][i]),
                                                                        (tabuleiro[5][i]),
                                                                        (tabuleiro[6][i])))
        print("_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")

    mostrar_tabuleiro(tabuleiro)
    i_0 = 5
    i_1 = 5
    i_2 = 5
    i_3 = 5
    i_4 = 5
    i_5 = 5
    i_6 = 5

    def VerificarTabuleiro(tabuleiro):
        verdadeiro = False
        ##### verificar todas as colunas##
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == tabuleiro[0][3] != " ":
            verdadeiro = True
        if tabuleiro[0][1] == tabuleiro[0][2] == tabuleiro[0][3] == tabuleiro[0][4] != " ":
            verdadeiro = True
        if tabuleiro[0][2] == tabuleiro[0][3] == tabuleiro[0][4] == tabuleiro[0][5] != " ":
            verdadeiro = True
        if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == tabuleiro[1][3] != " ":
            verdadeiro = True
        if tabuleiro[1][1] == tabuleiro[1][2] == tabuleiro[1][3] == tabuleiro[1][4] != " ":
            verdadeiro = True
        if tabuleiro[1][2] == tabuleiro[1][3] == tabuleiro[1][4] == tabuleiro[1][5] != " ":
            verdadeiro = True
        if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == tabuleiro[2][3] != " ":
            verdadeiro = True
        if tabuleiro[2][1] == tabuleiro[2][2] == tabuleiro[2][3] == tabuleiro[2][4] != " ":
            verdadeiro = True
        if tabuleiro[2][2] == tabuleiro[2][3] == tabuleiro[2][4] == tabuleiro[2][5] != " ":
            verdadeiro = True
        if tabuleiro[3][0] == tabuleiro[3][1] == tabuleiro[3][2] == tabuleiro[3][3] != " ":
            verdadeiro = True
        if tabuleiro[3][1] == tabuleiro[3][2] == tabuleiro[3][3] == tabuleiro[3][4] != " ":
            verdadeiro = True
        if tabuleiro[3][2] == tabuleiro[3][3] == tabuleiro[3][4] == tabuleiro[3][5] != " ":
            verdadeiro = True
        if tabuleiro[4][0] == tabuleiro[4][1] == tabuleiro[4][2] == tabuleiro[4][3] != " ":
            verdadeiro = True
        if tabuleiro[4][1] == tabuleiro[4][2] == tabuleiro[4][3] == tabuleiro[4][4] != " ":
            verdadeiro = True
        if tabuleiro[4][2] == tabuleiro[4][3] == tabuleiro[4][4] == tabuleiro[4][5] != " ":
            verdadeiro = True
        if tabuleiro[5][0] == tabuleiro[5][1] == tabuleiro[5][2] == tabuleiro[5][3] != " ":
            verdadeiro = True
        if tabuleiro[5][1] == tabuleiro[5][2] == tabuleiro[5][3] == tabuleiro[5][4] != " ":
            verdadeiro = True
        if tabuleiro[5][2] == tabuleiro[5][3] == tabuleiro[5][4] == tabuleiro[5][5] != " ":
            verdadeiro = True
        if tabuleiro[6][0] == tabuleiro[6][1] == tabuleiro[6][2] == tabuleiro[6][3] != " ":
            verdadeiro = True
        if tabuleiro[6][1] == tabuleiro[6][2] == tabuleiro[6][3] == tabuleiro[6][4] != " ":
            verdadeiro = True
        if tabuleiro[6][2] == tabuleiro[6][3] == tabuleiro[6][4] == tabuleiro[6][5] != " ":
            verdadeiro = True

            ##verificar todas as diagonais##
        if tabuleiro[3][0] == tabuleiro[2][1] == tabuleiro[1][2] == tabuleiro[0][3] != " ":
            verdadeiro = True
        if tabuleiro[4][0] == tabuleiro[3][1] == tabuleiro[2][2] == tabuleiro[1][3] != " ":
            verdadeiro = True
        if tabuleiro[5][0] == tabuleiro[4][1] == tabuleiro[3][2] == tabuleiro[2][3] != " ":
            verdadeiro = True
        if tabuleiro[6][0] == tabuleiro[5][1] == tabuleiro[4][2] == tabuleiro[3][3] != " ":
            verdadeiro = True
        if tabuleiro[3][0] == tabuleiro[4][1] == tabuleiro[5][2] == tabuleiro[6][3] != " ":
            verdadeiro = True
        if tabuleiro[2][0] == tabuleiro[3][1] == tabuleiro[4][2] == tabuleiro[5][3] != " ":
            verdadeiro = True
        if tabuleiro[1][0] == tabuleiro[2][1] == tabuleiro[3][2] == tabuleiro[4][3] != " ":
            verdadeiro = True
        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3] != " ":
            verdadeiro = True

        if tabuleiro[3][1] == tabuleiro[2][2] == tabuleiro[1][3] == tabuleiro[0][4] != " ":
            verdadeiro = True
        if tabuleiro[4][1] == tabuleiro[3][2] == tabuleiro[2][3] == tabuleiro[1][4] != " ":
            verdadeiro = True
        if tabuleiro[5][1] == tabuleiro[4][2] == tabuleiro[3][3] == tabuleiro[2][4] != " ":
            verdadeiro = True
        if tabuleiro[6][1] == tabuleiro[5][2] == tabuleiro[4][3] == tabuleiro[3][4] != " ":
            verdadeiro = True
        if tabuleiro[3][1] == tabuleiro[4][2] == tabuleiro[5][3] == tabuleiro[6][4] != " ":
            verdadeiro = True
        if tabuleiro[2][1] == tabuleiro[3][2] == tabuleiro[4][3] == tabuleiro[5][4] != " ":
            verdadeiro = True
        if tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3] == tabuleiro[4][4] != " ":
            verdadeiro = True
        if tabuleiro[0][1] == tabuleiro[1][2] == tabuleiro[2][3] == tabuleiro[3][4] != " ":
            verdadeiro = True

        if tabuleiro[3][2] == tabuleiro[2][3] == tabuleiro[1][4] == tabuleiro[0][5] != " ":
            verdadeiro = True
        if tabuleiro[4][2] == tabuleiro[3][3] == tabuleiro[2][4] == tabuleiro[1][5] != " ":
            verdadeiro = True
        if tabuleiro[5][2] == tabuleiro[4][3] == tabuleiro[3][4] == tabuleiro[2][5] != " ":
            verdadeiro = True
        if tabuleiro[6][2] == tabuleiro[5][3] == tabuleiro[4][4] == tabuleiro[3][5] != " ":
            verdadeiro = True
        if tabuleiro[3][2] == tabuleiro[4][3] == tabuleiro[5][4] == tabuleiro[6][5] != " ":
            verdadeiro = True
        if tabuleiro[2][2] == tabuleiro[3][3] == tabuleiro[4][4] == tabuleiro[5][5] != " ":
            verdadeiro = True
        if tabuleiro[1][2] == tabuleiro[2][3] == tabuleiro[3][4] == tabuleiro[4][5] != " ":
            verdadeiro = True
        if tabuleiro[0][2] == tabuleiro[1][3] == tabuleiro[2][4] == tabuleiro[3][5] != " ":
            verdadeiro = True

            #### Verificar linhas ##
        if tabuleiro[3][0] == tabuleiro[4][0] == tabuleiro[5][0] == tabuleiro[6][0] != " ":
            verdadeiro = True
        if tabuleiro[2][0] == tabuleiro[3][0] == tabuleiro[4][0] == tabuleiro[5][0] != " ":
            verdadeiro = True
        if tabuleiro[1][0] == tabuleiro[2][0] == tabuleiro[3][0] == tabuleiro[4][0] != " ":
            verdadeiro = True
        if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == tabuleiro[3][0] != " ":
            verdadeiro = True

        if tabuleiro[3][1] == tabuleiro[4][1] == tabuleiro[5][1] == tabuleiro[6][1] != " ":
            verdadeiro = True
        if tabuleiro[2][1] == tabuleiro[3][1] == tabuleiro[4][1] == tabuleiro[5][1] != " ":
            verdadeiro = True
        if tabuleiro[1][1] == tabuleiro[2][1] == tabuleiro[3][1] == tabuleiro[4][1] != " ":
            verdadeiro = True
        if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == tabuleiro[3][1] != " ":
            verdadeiro = True

        if tabuleiro[3][2] == tabuleiro[4][2] == tabuleiro[5][2] == tabuleiro[6][2] != " ":
            verdadeiro = True
        if tabuleiro[2][2] == tabuleiro[3][2] == tabuleiro[4][2] == tabuleiro[5][2] != " ":
            verdadeiro = True
        if tabuleiro[1][2] == tabuleiro[2][2] == tabuleiro[3][2] == tabuleiro[4][2] != " ":
            verdadeiro = True
        if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == tabuleiro[3][2] != " ":
            verdadeiro = True

        if tabuleiro[3][3] == tabuleiro[4][3] == tabuleiro[5][3] == tabuleiro[6][3] != " ":
            verdadeiro = True
        if tabuleiro[2][3] == tabuleiro[3][3] == tabuleiro[4][3] == tabuleiro[5][3] != " ":
            verdadeiro = True
        if tabuleiro[1][3] == tabuleiro[2][3] == tabuleiro[3][3] == tabuleiro[4][3] != " ":
            verdadeiro = True
        if tabuleiro[0][3] == tabuleiro[1][3] == tabuleiro[2][3] == tabuleiro[3][3] != " ":
            verdadeiro = True

        if tabuleiro[3][4] == tabuleiro[4][4] == tabuleiro[5][4] == tabuleiro[6][4] != " ":
            verdadeiro = True
        if tabuleiro[2][4] == tabuleiro[3][4] == tabuleiro[4][4] == tabuleiro[5][4] != " ":
            verdadeiro = True
        if tabuleiro[1][4] == tabuleiro[2][4] == tabuleiro[3][4] == tabuleiro[4][4] != " ":
            verdadeiro = True
        if tabuleiro[0][4] == tabuleiro[1][4] == tabuleiro[2][4] == tabuleiro[3][4] != " ":
            verdadeiro = True

        if tabuleiro[3][5] == tabuleiro[4][5] == tabuleiro[5][5] == tabuleiro[6][5] != " ":
            verdadeiro = True
        if tabuleiro[2][5] == tabuleiro[3][5] == tabuleiro[4][5] == tabuleiro[5][5] != " ":
            verdadeiro = True
        if tabuleiro[1][5] == tabuleiro[2][5] == tabuleiro[3][5] == tabuleiro[4][5] != " ":
            verdadeiro = True
        if tabuleiro[0][5] == tabuleiro[1][5] == tabuleiro[2][5] == tabuleiro[3][5] != " ":
            verdadeiro = True

        if tabuleiro[3][6] == tabuleiro[4][6] == tabuleiro[5][6] == tabuleiro[6][6] != " ":
            verdadeiro = True
        if tabuleiro[2][6] == tabuleiro[3][6] == tabuleiro[4][6] == tabuleiro[5][6] != " ":
            verdadeiro = True
        if tabuleiro[1][6] == tabuleiro[2][6] == tabuleiro[3][6] == tabuleiro[4][6] != " ":
            verdadeiro = True
        if tabuleiro[0][6] == tabuleiro[1][6] == tabuleiro[2][6] == tabuleiro[3][6] != " ":
            verdadeiro = True
        return verdadeiro

    for jogadas in range(1, 43):
        if jogadas % 2 != 0:
            while True:
                jogador_X = int(input("Qual é a coluna escolhida jogador X? "))
                if jogador_X == 0:
                    if tabuleiro[0][i_0] == " ":
                        tabuleiro[0][i_0] = itens[0]
                        i_0 = i_0 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_X == 1:
                    if tabuleiro[1][i_1] == " ":
                        tabuleiro[1][i_1] = itens[0]
                        i_1 = i_1 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_X == 2:
                    if tabuleiro[2][i_2] == " ":
                        tabuleiro[2][i_2] = itens[0]
                        i_2 = i_2 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_X == 3:
                    if tabuleiro[3][i_3] == " ":
                        tabuleiro[3][i_3] = itens[0]
                        i_3 = i_3 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_X == 4:
                    if tabuleiro[4][i_4] == " ":
                        tabuleiro[4][i_4] = itens[0]
                        i_4 = i_4 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_X == 5:
                    if tabuleiro[5][i_5] == " ":
                        tabuleiro[5][i_5] = itens[0]
                        i_5 = i_5 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_X == 6:
                    if tabuleiro[6][i_6] == " ":
                        tabuleiro[6][i_6] = itens[0]
                        i_6 = i_6 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                elif jogador_X > 6 or jogador_X < 0:
                    print("Essa coluna não é válida")
            if VerificarTabuleiro(tabuleiro):
                print("VOCÊ GANHOU JOGADOR X")
                break

        else:
            while True:
                jogador_O = int(input("Qual é a coluna escolhida jodador O? "))
                if jogador_O == 0:
                    if tabuleiro[0][i_0] == " ":
                        tabuleiro[0][i_0] = itens[1]
                        i_0 = i_0 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_O == 1:
                    if tabuleiro[1][i_1] == " ":
                        tabuleiro[1][i_1] = itens[1]
                        i_1 = i_1 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_O == 2:
                    if tabuleiro[2][i_2] == " ":
                        tabuleiro[2][i_2] = itens[1]
                        i_2 = i_2 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_O == 3:
                    if tabuleiro[3][i_3] == " ":
                        tabuleiro[3][i_3] = itens[1]
                        i_3 = i_3 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_O == 4:
                    if tabuleiro[4][i_4] == " ":
                        tabuleiro[4][i_4] = itens[1]
                        i_4 = i_4 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_O == 5:
                    if tabuleiro[5][i_5] == " ":
                        tabuleiro[5][i_5] = itens[1]
                        i_5 = i_5 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                if jogador_O == 6:
                    if tabuleiro[6][i_6] == " ":
                        tabuleiro[6][i_6] = itens[1]
                        i_6 = i_6 - 1
                        mostrar_tabuleiro(tabuleiro)
                        break
                    else:
                        print("Escolha uma coluna disponivel")
                elif jogador_O > 6 or jogador_O < 0:
                    print("Essa coluna não é válida")

            if VerificarTabuleiro(tabuleiro):
                print("VOCÊ GANHOU JOGADOR O")
                break


if __name__ == "__main__":
    JogoQuatroEmLinhas()
