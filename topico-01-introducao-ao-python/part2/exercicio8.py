# 8. Calcule a acurácia de cada classe da seguinte matriz de confusão:
# |       | Cat | Goat  | Cow | Dog |
# |---    |---  |---    |---  |---  |
# | Cat   | 50  | 20    | 2   | 10  |
# | Goat  | 40  | 70    | 20  | 15  |
# | Cow   | 10  | 30    | 40  | 5   |
# | Dog   | 5   | 10    | 30  | 50  |

from exercicio7 import gerar_matriz
import numpy as np


def acuracia(matriz_confusao):
  acuracias = []

  for i in range(len(matriz_confusao)):
    acuracias.append(matriz_confusao[i][i] / sum(matriz_confusao[i]))

  return acuracias


if __name__ == "__main__":
  matriz_confusao = np.array([[50, 20, 2, 10], [40, 70, 20, 15], [10, 30, 40, 5], [5, 10, 30, 50]])
  print(matriz_confusao)
  print(acuracia(matriz_confusao))

  matriz_confusao2 = np.array(gerar_matriz(10, 10))
  print(matriz_confusao2)
  print(acuracia(matriz_confusao2))
