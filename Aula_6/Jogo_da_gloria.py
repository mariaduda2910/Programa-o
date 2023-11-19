from random import *

tabuleiro = list(range(1, 64))
jogadores = ["amarelo", "azul", "verde", "vermelho", "branco"]
print(tabuleiro)


def JogarDados():
    dados_1 = randint(1, 7)
    dados_2 = randint(1, 7)
    jogada = dados_2 + dados_1
    return int(jogada)


# def CasasEspeciais(tabuleiro):
#     match tabuleiro:
#         case tabuleiro[5] == jogadores
#             jogadores[] =
#         case 6:
for i in range(len(jogadores)):
    jogadores_dados = int(input(f"Vamos la jogador {jogadores[i]}, jogue os dados: Pressione 1 para jogar os dados. "))
    if jogadores_dados == 1:
        index_da_jogada = JogarDados()
        print(f"Boa!!! O número do dado foi {index_da_jogada}")
        tabuleiro[index_da_jogada - 1] = jogadores[i]
        print(tabuleiro)
        # if tabuleiro[index_da_jogada - 1] == tabuleiro[0] or tabuleiro[index_da_jogada - 1] == tabuleiro[1] or\
        #     tabuleiro[index_da_jogada - 1] == tabuleiro[2] or tabuleiro[index_da_jogada - 1] == tabuleiro[3] or \
        #     tabuleiro[index_da_jogada - 1] == tabuleiro[4]:
        #     tabuleiro[index_da_jogada - 1] = jogadores[i] + tabuleiro[index_da_jogada - 1]
        #     print(tabuleiro)
        # if index_da_jogada == 4:
        #     jogador_travado = jogadores[i]
        #     print(tabuleiro)
        # if tabuleiro[index_da_jogada - 1] == jogadores:
        #     print(tabuleiro)


