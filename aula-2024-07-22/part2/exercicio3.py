# 3. Crie uma função que divida um vetor em duas partes

from exercicio1 import gerar_vetor

def divide_vetor_meio(vetor):
  tamanho = len(vetor)
  meio = tamanho // 2
  return vetor[:meio], vetor[meio:]

vetor = gerar_vetor()

parte1, parte2 = divide_vetor_meio(vetor)

print("Vetor Inicial:", vetor)
print("Parte 1:", parte1)
print("Parte 2:", parte2)
