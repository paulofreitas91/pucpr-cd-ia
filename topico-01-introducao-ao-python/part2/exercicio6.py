# 6. Crie todas as funçõee abaixo para manipular arrays
# - len()
# - max()
# - min()
# - mean()
# - avg()
# - remove_all_elem()

from exercicio1 import gerar_vetor
import random


def funcao_len(vetor):
  return len(vetor)


def funcao_max(vetor):
  return max(vetor)


def funcao_min(vetor):
  return min(vetor)


def funcao_mean(vetor):
  return sum(vetor) / len(vetor)


def funcao_avg(vetor):
  return sum(vetor) / len(vetor)


def funcao_remove_all_elem(vetor, elem):
  return [x for x in vetor if x != elem]


vetor = gerar_vetor(100)
remover = vetor[random.randint(0, len(vetor) - 1)]

print(vetor)
print(funcao_len(vetor))
print(funcao_max(vetor))
print(funcao_min(vetor))
print(funcao_mean(vetor))
print(funcao_avg(vetor))
print(funcao_remove_all_elem(vetor, remover), "Removido:", remover)
