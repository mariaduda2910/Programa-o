from random import *

tabuleiro = list(range(1, 64))
jogadores = ["amarelo", "azul", "verde", "vermelho", "branco"]
print(tabuleiro)


def JogarDados():
    dados_1 = randint(1, 7)
    dados_2 = randint(1, 7)
    jogada = dados_2 + dados_1
    return int(jogada)


for i in range(len(jogadores)):
    jogadores_dados = int(input(f"Vamos la jogador {jogadores[i]}, jogue os dados: Pressione 1 para jogar os dados. "))
    if jogadores_dados == 1:
        index_da_jogada = JogarDados()
        print(f"Boa!!! O número do dado foi {index_da_jogada}")
        # if tabuleiro[index_da_jogada - 1] == jogadores[0] or tabuleiro[index_da_jogada - 1] == jogadores[1] or \
        #         tabuleiro[index_da_jogada - 1] == jogadores[2] or tabuleiro[index_da_jogada - 1] == jogadores[3] or \
        #         tabuleiro[index_da_jogada - 1] == jogadores[4]:
            jogadores_casas = tabuleiro[index_da_jogada - 1]
            tabuleiro[index_da_jogada - 1] = jogadores_casas + jogadores[i]
            print("a",tabuleiro)
        else:
            tabuleiro[index_da_jogada - 1] = jogadores[i]
            print(tabuleiro)
