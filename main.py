import math
import pandas as pd

nodos = ["portal 80", "quirigua", "carrera 90", "Av cali", "granja-cr77", "Min de dios", "Boyaca", "Ferias", "Av 68", "Cra 53", "Cra 47", "Esc militar", "POLO"]

matriz_distancia = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0]]


with open("CoodernadasEstacioens.txt","r") as archivo:
    lineas = archivo.readlines()

coordenadas_x = []
coordenadas_y = []

for linea in lineas:

    partes = linea.strip().split()
    
    y = float(partes[0])
    x = float(partes[1])

    coordenadas_x.append(x)
    coordenadas_y.append(y)


for i in range(13):
    for j in range(13):
        matriz_distancia[i][j] = round(math.sqrt(math.pow(coordenadas_x[i]-coordenadas_x[j],2)+math.pow(coordenadas_y[i]-coordenadas_y[j],2))*100000,3)

df = pd.DataFrame(matriz_distancia, columns=nodos, index=nodos)

print(df)
