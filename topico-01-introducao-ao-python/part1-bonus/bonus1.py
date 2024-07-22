# BONUS: Comparativo referente ao uso de estruturas lógicas corretas

import time


def solucao1(interacoes=100000000):
  t1 = time.time()

  for i in range(interacoes):
    letra = 'a'

    if letra == 'a':
      letra = 1

    if letra == 'b':
      letra = 1

    if letra == 'c':
      letra = 1

    if letra == 'd':
      letra = 1

    if letra == 'e':
      letra = 1

    if letra == 'f':
      letra = 1

  t2 = time.time()

  return t2-t1


def solucao2(interacoes=100000000):
  t1 = time.time()

  for i in range(interacoes):
    letra = 'a'

    if letra == 'a':
      letra = 1

    elif letra == 'b':
      letra = 1

    elif letra == 'c':
      letra = 1

    elif letra == 'd':
      letra = 1

    elif letra == 'e':
      letra = 1

    elif letra == 'f':
      letra = 1

  t2 = time.time()

  return t2-t1


def solucao3(interacoes=100000000):
  t1 = time.time()

  while interacoes > 0:
    letra = 'a'

    if letra == 'a':
      letra = 1

    if letra == 'b':
      letra = 1

    if letra == 'c':
      letra = 1

    if letra == 'd':
      letra = 1

    if letra == 'e':
      letra = 1

    if letra == 'f':
      letra = 1

    interacoes -= 1

  t2 = time.time()

  return t2-t1


def solucao4(interacoes=100000000):
  t1 = time.time()
  i = 0

  while interacoes > 0:
    letra = 'a'

    if letra == 'a':
      letra = 1

    elif letra == 'b':
      letra = 1

    elif letra == 'c':
      letra = 1

    elif letra == 'd':
      letra = 1

    elif letra == 'e':
      letra = 1

    elif letra == 'f':
      letra = 1

    interacoes -= 1

  t2 = time.time()

  return t2-t1



interacoes = 100000000
opcao1 = solucao1(interacoes)
opcao2 = solucao2(interacoes)
opcao3 = solucao3(interacoes)
opcao4 = solucao4(interacoes)
melhor = min(opcao1, opcao2, opcao3, opcao4)

solucoes = {
  opcao1: "Solução 1",
  opcao2: "Solução 2",
  opcao3: "Solução 3",
  opcao4: "Solução 4"
}

solucao_mais_rapida = solucoes[melhor]
print(f"{solucao_mais_rapida} é a mais rápida")

for solucao, nome in solucoes.items():
  diferenca = solucao - melhor
  porcentagem = solucao / melhor * 100
  print(f"{nome}: {solucao:.5f}, diferença de {diferenca:.5f} | {porcentagem:.3f}")
