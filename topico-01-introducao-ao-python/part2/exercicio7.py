# 7. Calcule a média de cada linha e coluna de uma matriz NxM.

from exercicio1 import gerar_vetor
import time
import numpy as np


def gerar_matriz(linhas=3, colunas=3, min=0, max=10):
  matriz = []

  for _ in range(linhas):
    matriz.append(gerar_vetor(colunas, min, max))

  return matriz


def media_linha(matriz):
  return np.mean(matriz, axis=1)


def media_linha_v2(matriz):
  media = []

  for linha in matriz:
    media.append(sum(linha) / len(linha))

  return media


def media_coluna(matriz):
  return np.mean(matriz, axis=0)


def media_coluna_v2(matriz):
  tamanho = len(matriz[0])
  media = [0 for _ in range(tamanho)]

  for linha in matriz:
    for coluna in range(len(linha)):
      media[coluna] += linha[coluna]

  for i in range(tamanho):
    media[i] /= len(matriz)

  return media


if __name__ == "__main__":
  matriz = np.array(gerar_matriz(1000, 10000, 0, 1000))
  matriz2 = gerar_matriz(1000, 10000, 0, 1000)


  inicio_1 = time.time()
  matriz_linha = media_linha(matriz)
  matriz_coluna = media_coluna(matriz)
  fim_1 = time.time()


  inicio_2 = time.time()
  matriz_linha2 = media_linha_v2(matriz2)
  matriz_coluna2 = media_coluna_v2(matriz2)
  fim_2 = time.time()



  # print(matriz)
  # print(matriz_linha)
  # print(matriz_coluna)
  print(f"Tempo de execução: {(fim_1-inicio_1):0>8.8f} segundos. Utilizando numpy")

  # print(matriz2)
  # print(media_linha_v2(matriz2))
  # print(media_coluna_v2(matriz2))
  print(f"Tempo de execução: {(fim_2-inicio_2):0>8.8f} segundos. Sem utilizar numpy")
