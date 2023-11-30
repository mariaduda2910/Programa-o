from random import *

jogadores = ["amarelo", "azul", "verde", "vermelho", "branco"]
tabuleiro = list(range(1, 64))
tabuleiro[0] = "amarelo", "azul", "verde", "vermelho", "branco"


def JogarDados():
    dados_1 = randint(1, 7)
    dados_2 = randint(1, 7)
    jogada = dados_2 + dados_1
    return int(jogada)

def search (lista, valor):
    for valor in lista:
        return lista.index(valor)

print(tabuleiro)
while True:
    for i in range(len(jogadores)):
        jogadores_dados = int(
            input(f"Vamos la jogador {jogadores[i]}, jogue os dados: Pressione 1 para jogar os dados. "))
        if jogadores_dados == 1:
            jogar_dados = JogarDados()
            print(f"Boa!!! O número do dado foi {jogar_dados}")
            index = search(tabuleiro,jogadores[i])
            # index = tabuleiro.index(jogadores[i])
            jogador_removido = jogadores[i]
            tabuleiro.remove(jogador_removido)
            tabuleiro[index] = index + 1
            jogo = JogarDados()
            print("dados", jogo)
            jogas_posteriores = index + jogo
            print(jogas_posteriores)
            tabuleiro[jogas_posteriores] = jogadores
            print(tabuleiro)

            # except ValueError:
            #     print("erro")

