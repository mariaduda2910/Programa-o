itens = ["X","O"]
tabuleiro = [1, 2, 3, 4, 5, 6, 7], \
    [8, 9, 10, 11, 12, 13, 14], \
    [15, 16, 17, 18, 19, 20, 21], \
    [22, 23, 24, 25, 26, 27, 28], \
    [29, 30, 31, 32, 33, 34, 35], \
    [36, 37, 38, 39, 40, 41, 42]


coluna_1 = [1, 8, 15, 22, 29, "X"]
jogador = int(input("valor?"))
valor_maior = None

# while True:
# #     jogador = int(input("valor?"))
# for num in coluna_1:
#     if valor_maior is None or num > valor_maior:
#         valor_maior = itens[0]

ultimo = (max(coluna_1))
print(ultimo)
# jogador = int(input("valor?"))
while True:
    if coluna_1[5] > coluna_1[4]:
        coluna_1[5] = itens[0]
        if coluna_1[4] > coluna_1 [3]:
            coluna_1[4] = itens[0]
            if coluna_1[3] > coluna_1[2]:
                coluna_1[3] = itens[0]
                if coluna_1[2] > coluna_1[1]:
                    coluna_1[2] = itens[0]
                    if coluna_1[1] > coluna_1[0]:
                        coluna_1[1] = itens[0]
                    else:
                        coluna_1[0] = itens[0]
print(coluna_1)

# for coluna_1 in range(6):
#
#     jogador = int(input("valor?"))
#     if jogador == 1:
#         coluna_1[5] = itens[0]
#     if coluna_1[-1] == "X":
#         coluna_1[4] = itens[0]
#     if coluna_1[-1] == "X":
#         coluna_1[3] = itens[0]
#     if coluna_1[-1] == "X":
#         coluna_1[2] = itens[0]
#     if coluna_1[-1] == "X":
#         coluna_1[1] = itens[0]
#     if coluna_1[-1] == "X":
#         coluna_1[0] = itens[0]
    print(coluna_1)
if jogador == 2:
    coluna_1[-1 != "X"] = itens[0]
    print(coluna_1)

for i in range(42):
    i = i + 1
    tabuleiro.append(i)

if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == tabuleiro[0][3]:
    print("Você ganhou!!! Jogador {}".format(ganhador))
    break
