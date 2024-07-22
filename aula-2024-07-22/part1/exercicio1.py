# 1. Calcule a idade a partir do ano de nascimento

import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = datetime.datetime.now().year

print(f"A idade é: {ano_atual - ano_nascimento}")
