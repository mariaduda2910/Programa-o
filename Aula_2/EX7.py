# Implemente um programa para modelar o funcionamento de uma máquina. Sendo que
# quando da inserção das letras: ’L’, ’D’ e ’F’, são apresentadas, respetivamente, as
# mensagens: “Ligar”, “Desligar” e “Furar” (use if…else).
maquina = (input("LIGAR(L), DESLIGAR(D), FURAR(F)")).upper()
if maquina == "L":
    print("LIGADO")
elif maquina == "D":
    print("DESLIGADO")
elif maquina == "F":
    print("FURANDO")

# maquina = (input("LIGAR(L), DESLIGAR(D), FURAR(F)"))
# maquina = maquina.upper()
# while maquina == "D":
#     maquina = input(("A máquina não foi ligada, caso deseje ligar a maquina pressione o botão (L)"))
#     if maquina == "L":
#         maquina = "L"
#         break#como fazer o programa voltar la pra cima
#     elif maquina == "F":
#         print("Primeiro pressione (L) para ligar a maquina")
# if maquina == "L":
#     ligada = input(("Voce ligou a maquina, caso deseje furar aperte o botao F, se deseja desligar pressione o botao D"))
#     ligada = ligada.upper()
#     if ligada == "F":
#         print("FURANDO...")
#     elif ligada == "D" :
#         print("DESLIGANDO...")