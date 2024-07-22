# 2. Escreva um programa que solicite ao usuário que digite uma temperatura em graus Celsius, converta essa temperatura para Fahrenheit e exiba o resultado.

def celsius_para_fahrenheit(celsius):
  return celsius * 9/5 + 32


if __name__ == "__main__":
  celsius = float(input("Digite a temperatura em Celsius: "))

  print(f"A temperatura em Fahrenheit é: {celsius_para_fahrenheit(celsius)}")
