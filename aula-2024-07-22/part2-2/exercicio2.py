# 2. Dado um arquivo contendo números aleatórios, calcule a média, mediana e desvio padrão

from exercicio1 import salvar_vetor_arquivo
import pickle
import time


def ler_vetor_de_arquivo_pkl(nome_arquivo):
  with open(nome_arquivo, "rb") as fd:
    return pickle.load(fd)


def ler_vetor_de_arquivo_txt(nome_arquivo):
  with open(nome_arquivo, "r") as fd:
    vetor = [int(x) for x in fd.read().split()]

  return vetor


def calcular_media(vetor):
  return sum(vetor) / len(vetor)


def calcular_mediana(vetor):
  vetor_ordenado = sorted(vetor)
  tamanho = len(vetor_ordenado)

  if tamanho % 2 == 0:
    return (vetor_ordenado[tamanho // 2] + vetor_ordenado[tamanho // 2 - 1]) / 2
  else:
    return vetor_ordenado[tamanho // 2]


def calcular_moda(vetor):
  return max(set(vetor), key=vetor.count)


def calcular_desvio_padrao(vetor):
  media = calcular_media(vetor)
  return (sum([(x - media) ** 2 for x in vetor]) / len(vetor)) ** 0.5


nome_arquivo = "vetor"
salvar_vetor_arquivo(nome_arquivo, 1000000, 0, 1000)

inicio_pickle = time.time()
vetor_pickle = ler_vetor_de_arquivo_pkl(f"{nome_arquivo}.pkl")
fim_pickle = time.time()
tempo_pickle = fim_pickle - inicio_pickle
print(f"Tempo de execução com pkl: {tempo_pickle:.5f} segundos")

inicio_txt = time.time()
vetor_txt = ler_vetor_de_arquivo_txt(f"{nome_arquivo}.txt")
fim_txt = time.time()
tempo_txt = fim_txt - inicio_txt
print(f"Tempo de execução com txt: {tempo_txt:.5f} segundos")

inicio_media = time.time()
media = calcular_media(vetor_pickle)
fim_media = time.time()

inicio_mediana = time.time()
mediana = calcular_mediana(vetor_pickle)
fim_mediana = time.time()

inicio_moda = time.time()
moda = calcular_moda(vetor_pickle)
fim_moda = time.time()

inicio_desvio = time.time()
desvio_padrao = calcular_desvio_padrao(vetor_pickle)
fim_desvio = time.time()

print(f"Tempo de execução: {(fim_media - inicio_media):0>8.5f} segundos. Média {media:.5f}")
print(f"Tempo de execução: {(fim_mediana - inicio_mediana):0>8.5f} segundos. Mediana {mediana:.5f}")
print(f"Tempo de execução: {(fim_moda - inicio_moda):0>8.5f} segundos. Moda {moda:.5f}")
print(f"Tempo de execução: {(fim_desvio - inicio_desvio):0>8.5f} segundos. Desvio Padrão {desvio_padrao:.5f}")
