# 4. Determine quantos múltiplos de 3 existem entre 0 e 100

multiplos = [i for i in range(0, 101) if i % 3 == 0]

print(f"Existem {len(multiplos)} múltiplos de 3 entre 0 e 100:")

for i in multiplos:
  print(i)
