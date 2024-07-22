# 4.  Crie uma função que divida um vetor em 3 partes, de acordo com uma razão (i.e 60%,20%,20%)

from exercicio1 import gerar_vetor


def divide_vetor_tres_partes(vetor, razao1=0.6, razao2=0.2):
  tamanho = len(vetor)
  parte1 = int(tamanho * razao1)
  parte2 = int(tamanho * razao2)
  return vetor[:parte1], vetor[parte1:parte1 + parte2], vetor[parte1 + parte2:]


vetor = gerar_vetor()

parte1, parte2, parte3 = divide_vetor_tres_partes(vetor)

print("Vetor Inicial:", vetor)
print("Parte 1:", parte1)
print("Parte 2:", parte2)
print("Parte 3:", parte3)
