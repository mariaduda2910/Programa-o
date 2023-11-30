# Exercício
# Ao exercício anterior adicione o jogo da batalha naval
# (https://pt.wikipedia.org/wiki/Batalha_naval_(jogo)),com 2 vertentes:
# (a) Jogador vs Computador: o computador deve escolher a posição onde são
# colocados os barcos, o computador escolhe as posições dos tiros aleatoriamente
# (opção: ou com algumas regras).
# (b) Jogador1 vs Jogador2: cada jogador escolhe a posição dos seus barcos.
# https://www.youtube.com/watch?v=EGmlFdwD4C4 TODO fazer tabuleiro
tabuleiro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def MostrarTabuleiro(tabuleiro):
    for l in range(0, 3):
        for C in range(0, 3):
            tabuleiro[l][C] = 1
    for l in range(0, 3):
        for c in range(0, 3):
            print(f"[{tabuleiro[l][c]:^6}]", end="")
        print()
