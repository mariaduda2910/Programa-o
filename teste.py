from random import randint

jogadores = ["amarelo", "azul", "verde", "vermelho", "branco"]
tabuleiro = {list(range(1, 64))}
print(tabuleiro.keys())
print(tabuleiro.values())
print(tabuleiro.items())

def JogarDados():
    return randint(1, 6) + randint(1, 6)


def PrimeiraRodada(jogarDados, jogador):
    global tabuleiro
    jogada = jogarDados - 1
    if type(tabuleiro[jogada]) == int:
        tabuleiro[jogada] = jogador
    else:
        tabuleiro[jogada] = jogador + " " + tabuleiro[jogada]
    print(tabuleiro)


count = 0

for i in range(len(jogadores)):
    input(f"Vamos la jogador {jogadores[i]}, jogue os dados: Pressione Enter para jogar os dados. ")
    jogarDados = JogarDados()
    print(f"Boa!!! O número do dado foi {jogarDados}")
    jogador = jogadores[i]
    PrimeiraRodada(jogarDados, jogador)
    count = + 1
    if count == 4:
        break
for i in range(len(jogadores)):
    input(f"Vamos la jogador {jogadores[i]}, jogue os dados: Pressione 1 para jogar os dados. ")
    jogarDados = JogarDados()
    print(f"Boa!!! O número do dado foi {jogarDados}")
    index = tabuleiro.index(jogadores[i])
    print(index)
    jogador_removido = jogadores[i]
    print(jogador_removido)
    tabuleiro.remove(jogador_removido)
    tabuleiro[index] = index + 1
    jogo = JogarDados()
    print("dados", jogo)
    jogas_posteriores = index + jogo
    print(jogas_posteriores)
    tabuleiro[jogas_posteriores] = jogadores[i]
    print(tabuleiro)

#fazer o tabuleiro em dicionário
#del para apagar
#