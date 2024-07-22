# 6. Dado um certo números de passageiros, determine um função que calcula quantos ônibus serão necessários para acomoda-los

def calcula_onibus(n_passageiros):
  return n_passageiros // 40 + 1

n_passageiros = int(input("Digite o número de passageiros: "))

print(f"Serão necessários {calcula_onibus(n_passageiros)} ônibus para acomodar {n_passageiros} passageiros")
