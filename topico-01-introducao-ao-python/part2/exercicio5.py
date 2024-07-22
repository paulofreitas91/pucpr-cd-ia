# 5. Crie uma função que embaralha dois vetores

from exercicio1 import gerar_vetor
import random


def embaralhar_vetores(vetor1, vetor2):
  vetor_combinado = vetor1 + vetor2
  random.shuffle(vetor_combinado)

  return vetor_combinado


vetor1 = gerar_vetor()
vetor2 = gerar_vetor()

vetor_embaralhado = embaralhar_vetores(vetor1, vetor2)

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor Embaralhado:", vetor_embaralhado)
