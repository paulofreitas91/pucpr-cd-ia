# 1. Determine se um número é par ou impar

numero = int(input("Digite um número: "))

print(f"O número é {numero % 2 == 0 and 'par' or 'ímpar'}")
