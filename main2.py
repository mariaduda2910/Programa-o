from random import *

tabuleiro = list(range(1, 64))
jogadores = ["amarelo", "azul", "verde", "vermelho", "branco"]

def JogarDados():
    dados_1 = randint(1, 7)
    dados_2 = randint(1, 7)

    return randint(1, 6) + randint(1, 6)
i = 0
tabuleiro[0] = jogadores
print(tabuleiro)
while True:
    for i in range(len(tabuleiro)):
        jogadores_dados = int(input(f"Vamos la jogador {tabuleiro[0][i]}, jogue os dados: Pressione 1 para jogar os dados. "))
        if jogadores_dados == 1:
            index = tabuleiro[0].index(jogadores[0])
            jogador_removido = jogadores[0]
            tabuleiro[0].remove(jogador_removido)
            print("jogador removido", jogador_removido)
            jogar_dados = JogarDados()
            jogada = index + jogar_dados - 1
            print(f"Boa!!! O número do dado foi {jogar_dados}")
            tabuleiro[jogada] = jogador_removido
            print(tabuleiro)
            print(i)
##Falta fazer o i sempre valer 0

##Salvar o local das casas em variaveis
##fazer soma pra chegar nas casas

