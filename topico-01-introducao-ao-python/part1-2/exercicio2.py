# 2. Calcule a comissão de um vendedor, de acordo com a tabela abaixo:
# - 3,5% para vendas até R$ 5.000,00
# - 4,5% para vendas até R$ 10.000,00
# - 6% para vendas acima de R$ 10.000,00

vendas = float(input("Digite o valor das vendas: "))

if vendas <= 5000:
  comissao = vendas * 0.035
elif vendas <= 10000:
  comissao = vendas * 0.045
else:
  comissao = vendas * 0.06

print(f"A comissão é de R$ {comissao:.2f}")
