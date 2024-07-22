# 3. No cálculo acima, imprime até a quinta casa decimal

from exercicio2 import celsius_para_fahrenheit

celsius = float(input("Digite a temperatura em Celsius: "))

print(f"A temperatura em Fahrenheit é: {celsius_para_fahrenheit(celsius):.5f}")
