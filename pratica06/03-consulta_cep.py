"""
3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.
"""

import requests

try:
  cep = input("Informe um CEP(apenas número, sem traço): ")
  
  if not cep.isdigit():
    raise ValueError

  response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
  
  if response.status_code == 200:
    dados = response.json()

    if 'erro' in dados:
      print(f"O cep {cep} não existe!")
      exit()

    logradouro = f"{dados['logradouro']}"
    bairro = f"{dados['bairro']}"
    cidade = f"{dados['localidade']}"
    estado = f"{dados['estado']}"
    cep_formatado = f"{dados['cep']}"
    print(f"Logradouro: {logradouro} \nBairro: {bairro} \nCidade:{cidade} \nEstado: {estado} \nCEP: {cep_formatado}")
  else:
    print(f"Falha na requisição! Código de erro: {response.status_code}")
except ValueError:
  print("Informe apenas número!") 