from random import randint

jogadores = ["amarelo", "azul", "verde", "vermelho", "branco"]
posicoesJogadores = {jogador: 0 for jogador in jogadores}
tamanhoTabuleiro = 63
bloqueio = 0

def JogarDados():
    return randint(1, 6) + randint(1, 6)


def AtualizarPosicao(jogador, jogada):
    posicaoAtual = posicoesJogadores[jogador]
    novaPosicao = posicaoAtual + jogada
    if novaPosicao > tamanhoTabuleiro:
        novaPosicao = tamanhoTabuleiro - (novaPosicao - tamanhoTabuleiro)
    posicoesJogadores[jogador] = novaPosicao
    MotrarTabuleiro()
    print(posicoesJogadores)
    print(f"Jogador {jogador} move para a posição {novaPosicao}")


def MotrarTabuleiro():
    tabuleiro_temporario = list(range(0, 64))
    amarelo = posicoesJogadores["amarelo"]
    verde = posicoesJogadores["verde"]
    azul = posicoesJogadores["azul"]
    vermelho = posicoesJogadores["vermelho"]
    branco = posicoesJogadores["branco"]

    tabuleiro_temporario[amarelo] = jogadores[0]
    tabuleiro_temporario[azul] = jogadores[1]
    tabuleiro_temporario[verde] = jogadores[2]
    tabuleiro_temporario[vermelho] = jogadores[3]
    tabuleiro_temporario[branco] = jogadores[4]

    if amarelo == azul or amarelo == verde or amarelo == vermelho or amarelo == branco:
        jogador_atual = str(tabuleiro_temporario[amarelo])
        tabuleiro_temporario[amarelo] = jogador_atual + ", " + jogadores[0]
        print(tabuleiro_temporario)

    elif azul == verde or azul == vermelho or azul == branco:
        jogador_atual_1 = str(tabuleiro_temporario[azul])
        tabuleiro_temporario[azul] = jogador_atual_1 + ", " + jogadores[1]
        print(tabuleiro_temporario)
    elif verde == vermelho or verde == branco:
        jogador_atual_2 = str(tabuleiro_temporario[verde])
        tabuleiro_temporario[verde] = jogador_atual_2 + ", " + jogadores[2]
        print(tabuleiro_temporario)
    elif vermelho == branco:
        jogador_atual_3 = str(tabuleiro_temporario[vermelho])
        tabuleiro_temporario[vermelho] = jogador_atual_3 + ", " + jogadores[3]
        print(tabuleiro_temporario)

    else:
        print(tabuleiro_temporario)
    return


def RegrasDasCasas(jogador):
    if posicoesJogadores[jogador] == 5:
        print("fica uma vez sem jogar os dados")
        jogadorBloqueado = jogador
        posicoesJogadores[jogador] = 5
        return jogadorBloqueado
    elif posicoesJogadores[jogador] == 6:
        print("Ganhaste uma carona!!! Vamos para casa 12")
        posicoesJogadores[jogador] = 12
    elif posicoesJogadores[jogador] == 42:
        print("Avariou o trator volte para casa 30")
        posicoesJogadores[jogador] = 30
    elif posicoesJogadores[jogador] == 58:
        print("ups! Iniciaremos de novo nossa viagem")
        posicoesJogadores[jogador] = 0
    return

def Jogar():
    while True:
        for jogador in jogadores:
            input(f"Vez do jogador {jogador}. Pressione Enter para jogar os dados.")
            jogada = JogarDados()
            print(f"Jogador {jogador} tirou {jogada} nos dados.")
            RegrasDasCasas(jogador)
            AtualizarPosicao(jogador, jogada)
            if RegrasDasCasas(jogador) == jogador:
                break
            if posicoesJogadores[jogador] == tamanhoTabuleiro:
                print(f"Jogador {jogador} ganhou o jogo!")
                return


Jogar()

# TODO Preciso colocar mais de um jogador em uma msm casa
# TODO Preciso fazer o programa deixar um jogador sem jogar
