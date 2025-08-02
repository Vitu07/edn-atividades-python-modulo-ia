"""
4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.

"""
import json

dicionario_pessoa = {"Nome": "Ayrton","idade": 33,"cidade": "São Paulo"}

nome_arquivo = input("Informe o nome do arquivo: ")

if not(".json" in nome_arquivo):
  nome_arquivo = nome_arquivo + ".json"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json:
  json.dump(dicionario_pessoa, arquivo_json, ensure_ascii=False, indent=4)
  
with open(nome_arquivo, "r", encoding="utf-8") as arquivo_json:
  conteudo = json.load(arquivo_json)
  print(conteudo)