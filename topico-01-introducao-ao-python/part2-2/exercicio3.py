# 3. Carregue o arquivo 'exemplo.csv' em um array qualquer

import csv

def carregar_arquivo_csv(nome_arquivo):
  with open(nome_arquivo, "r") as fd:
    return list(csv.reader(fd))
  
nome_arquivo = "vetor.csv"

vetor = carregar_arquivo_csv(nome_arquivo)

print(vetor)
