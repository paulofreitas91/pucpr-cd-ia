# 1. Crie um array aleatório de 1000 posições e salve em um arquivo: a) linha a linha, b) pickle

import pickle
import random


def gerar_vetor(tamanho=10, min=0, max=100):
  return [random.randint(min, max) for _ in range(tamanho)]


def salvar_vetor_arquivo(nome_arquivo="vetor", tamanho=1000, min=0, max=100):
  vetor = gerar_vetor(tamanho, min, max)

  fd = open(f"{nome_arquivo}.txt", "w")
  for item in vetor:
    fd.write(f"{item}\n")
  fd.close()

  fd = open(f"{nome_arquivo}.pkl", "wb")
  pickle.dump(vetor, fd)
  fd.close()


if __name__ == "__main__":
  salvar_vetor_arquivo()
