# 7. Dado um numeral, calcule a soma de seus dígitos ==> 4782 => 4 + 7 + 8 + 2 =>  21

numero = input("Digite um número: ")
soma = 0

for i in numero:
  soma += int(i)

print(f"A soma dos dígitos de {numero} é {soma}")
