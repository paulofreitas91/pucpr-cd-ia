# 6. Crie todas as funçõee abaixo para manipular arrays
# - len()
# - max()
# - min()
# - mean()
# - avg()

from exercicio1 import gerar_vetor


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


vetor = gerar_vetor(10)

print(vetor)
print(funcao_len(vetor))
print(funcao_max(vetor))
print(funcao_min(vetor))
print(funcao_mean(vetor))
print(funcao_avg(vetor))
