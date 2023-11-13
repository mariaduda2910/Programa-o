def mostrar_tabuleiro():
    tabuleiro = [["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""], ["", "", "", "", "", "", ""],
                 ["", "", "", "", "", "", ""]]
    print("_=_=_=_=_=_=_=_=_=_=_=_=\n |0 |1 |2 |3 |4 |5 |6 |")
    print(" | {0} | {1} | {2} | {3} | {4} | {5} | {6} |".format((tabuleiro[0][0]),
                                                                                          (tabuleiro[1][0]),
                                                                                          (tabuleiro[2][0]),
                                                                                          (tabuleiro[3][0]),
                                                                                          (tabuleiro[4][0]),
                                                                                          (tabuleiro[5][0]),
                                                                                          (tabuleiro[6][0])))
    print(" | {0} | {1} | {2} | {3} | {4} | {5} | {6} |".format((tabuleiro[0][1]),
                                                                (tabuleiro[1][1]),
                                                                (tabuleiro[2][1]),
                                                                (tabuleiro[3][1]),
                                                                (tabuleiro[4][1]),
                                                                (tabuleiro[5][1]),
                                                                (tabuleiro[6][1])))
    print(" | {0} | {1} | {2} | {3} | {4} | {5} | {6} |".format((tabuleiro[0][1]),
                                                                (tabuleiro[1][2]),
                                                                (tabuleiro[2][2]),
                                                                (tabuleiro[3][2]),
                                                                (tabuleiro[4][2]),
                                                                (tabuleiro[5][2]),
                                                                (tabuleiro[6][2])))
    print(" | {0} | {1} | {2} | {3} | {4} | {5} | {6} |".format((tabuleiro[0][1]),
                                                                (tabuleiro[1][3]),
                                                                (tabuleiro[2][3]),
                                                                (tabuleiro[3][3]),
                                                                (tabuleiro[4][3]),
                                                                (tabuleiro[5][3]),
                                                                (tabuleiro[6][3])))
    print(" | {0} | {1} | {2} | {3} | {4} | {5} | {6} |".format((tabuleiro[0][1]),
                                                                (tabuleiro[1][4]),
                                                                (tabuleiro[2][4]),
                                                                (tabuleiro[3][4]),
                                                                (tabuleiro[4][4]),
                                                                (tabuleiro[5][4]),
                                                                (tabuleiro[6][4])))
    print(" | {0} | {1} | {2} | {3} | {4} | {5} | {6} |\n_=_=_=_=_=_=_=_=_=_=_=_=".format((tabuleiro[0][1]),
                                                                                          (tabuleiro[1][5]),
                                                                                          (tabuleiro[2][5]),
                                                                                          (tabuleiro[3][5]),
                                                                                          (tabuleiro[4][5]),
                                                                                          (tabuleiro[5][5]),
                                                                                          (tabuleiro[6][5])))


mostrar_tabuleiro()
