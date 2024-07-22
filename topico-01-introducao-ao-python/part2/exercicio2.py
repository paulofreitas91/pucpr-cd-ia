import random
from exercicio1 import gerar_vetor


def trocar_posicoes(vetor, pos1, pos2):
  if pos1 < 0 or pos2 < 0 or pos1 >= len(vetor) or pos2 >= len(vetor):
    print("Posições inválidas.")
    return vetor

  vetor[pos1], vetor[pos2] = vetor[pos2], vetor[pos1]
  return vetor


vetor = gerar_vetor()
pos_1 = random.randint(0, len(vetor)-1)
pos_2 = random.randint(0, len(vetor)-1)

print("Posições a serem trocadas: ", pos_1, pos_2)
print("Vetor inicial:\n", vetor)

trocar_posicoes(vetor, pos_1, pos_2)

print("Vetor final:\n", vetor)
