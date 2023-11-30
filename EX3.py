from random import *

jogadores = ["amarelo", "azul", "verde", "vermelho", "branco"]
tabuleiro = list(range(1, 64))
amarelo = 0
azul = 0
verde = 0
vermelho = 0
branco = 0


def JogarDados():
    dados_1 = randint(1, 7)
    dados_2 = randint(1, 7)
    jogada = dados_2 + dados_1
    return int(jogada)

while True:
    for i in range(len(jogadores)):
        jogadores_dados = int(input(f"Vamos la jogador {jogadores[i]}, jogue os dados: Pressione 1 para jogar os dados. "))
        if jogadores_dados == 1:
            for i in range(6):
                jogar_dados = JogarDados()
                print(f"Boa!!! O número do dado foi {jogar_dados}")
                jogada = jogar_dados - 1
                if type(tabuleiro[jogada]) == int:
                    tabuleiro[jogada] = jogadores[i]
                else:
                    tabuleiro[jogada] = jogadores[i], tabuleiro[jogada]
                print(tabuleiro)
        try:
            index = tabuleiro.index(jogadores)
            jogador_removido = jogadores
            tabuleiro.remove(jogador_removido)
            tabuleiro[index] = index + 1
            jogo = JogarDados()
            print("dados", jogo)
            jogas_posteriores = index + jogo
            print(jogas_posteriores)
            tabuleiro[jogas_posteriores] = jogadores
            print(tabuleiro)
        except ValueError:
            print("erro")
