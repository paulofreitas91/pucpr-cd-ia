# 1.  Crie um array de 10 posições

import random


def gerar_vetor(tamanho=10, min=0, max=100):
  return [random.randint(min, max) for _ in range(tamanho)]


if __name__ == "__main__":
  print(gerar_vetor())
