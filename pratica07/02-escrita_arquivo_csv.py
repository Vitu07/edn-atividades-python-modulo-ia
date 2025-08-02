"""
2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.
"""

import csv

dados = [["Vicente", 13 , "Santos"],["Maria", 20, "São Paulo"],["Ronaldo", 40,"Rio de janeiro"]]

nome_arquivo = input("Informe o nome do arquivo: ")

if not(".csv" in nome_arquivo):
  nome_arquivo = nome_arquivo + ".csv"

with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo_csv:
  escritor = csv.writer(arquivo_csv)
  escritor.writerow(["Nome", "Idade", "Cidade"])
  escritor.writerows(dados)
  print(f"Nome do arquivo csv: {nome_arquivo}")