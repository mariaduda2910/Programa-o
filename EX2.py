#Faça o algoritmo: Calcule a distância entre dois pontos, sendo que cada ponto é
#definido pelas coordenadas (x,y), i.e., ponto 1 (x1,y1) e ponto 2 (x2,y2), utilizando a
#seguinte fórmula: distancia = raiz((x2 − x1)^2 + (y2 − y1)^2).
import math

coordenada_1 = float(input("Qual o valor das coordenadas X1"))
coordenada_2 = float(input("Qual o valor das coordenadas X2"))
coordenada_3 = float(input("Qual o valor das coordenadas Y1"))
coordenada_4 = float(input("Qual o valor das coordenadas Y2"))
distancia = math.sqrt((coordenada_2 - coordenada_1)**2 + (coordenada_4 - coordenada_3)**2)

if distancia == 0:
    print("Os pontos estão sobrepostos")
else:
    print("A distancia é", distancia)
