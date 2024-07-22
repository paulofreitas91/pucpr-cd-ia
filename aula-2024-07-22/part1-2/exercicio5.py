# 5. Solicite números ao usuário, até que soma ultrapasse 1000

soma = 0

while soma <= 1000:
  numero = int(input("Digite um número: "))
  soma += numero
  print(f"A soma dos números digitados é {soma}\n")
