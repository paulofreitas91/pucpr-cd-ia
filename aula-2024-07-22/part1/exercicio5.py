# 5. Gere um número aleatório e determine o resto da divisão por 5

import random

numero = random.randint(0, 100000)
resto = numero % 5

print(f"O resto da divisão de {numero} por 5 é: {resto}")
