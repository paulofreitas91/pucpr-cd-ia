# 6. Fique sorteando números até o numeral 30 ser sorteado.

import random

numero = 0
contar = 0

while numero != 30:
  numero = random.randint(0, 1000)
  print(numero)
  contar += 1

print(f"O número 30 foi sorteado após {contar} tentativas")
