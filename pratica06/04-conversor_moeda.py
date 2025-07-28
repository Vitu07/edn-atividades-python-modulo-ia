"""
4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""

import datetime
import requests

API_KEY = "4c0cbbade1631cc50f6e2c4d65f17694a0f0aaa1162911d673ccc620c8856395"

moeda_estrangeira = input("Informe o código da moéda estrangeira: ").upper()
response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda_estrangeira}-BRL?token={API_KEY}")

if(response.status_code == 200):
  dados = response.json()[f'{moeda_estrangeira}BRL']
  cotacao_atual = f"{dados['bid']}"
  valor_maximo = f"{dados['high']}"
  valor_minimo = f"{dados['low']}"
  data_hora_atualizacao = f"{dados['create_date']}"
  cotacao_atual = float(cotacao_atual)
  valor_maximo = float(valor_maximo)
  valor_minimo = float(valor_minimo)

  data_obj = datetime.datetime.strptime(data_hora_atualizacao,"%Y-%m-%d %H:%M:%S" )
  data_formatada = data_obj.strftime("%d-%m-%Y %H:%M:%S")
  print(f"Cotação atual: {cotacao_atual:.2f} \nMaior valor de cotação: {valor_maximo:.2f} \nMenor valor de cotação: {valor_minimo:.2f} \nData e hora da ultima atualização: {data_formatada}")
elif (response.status_code == 404):
  print("Moeda não existe, por favor informe um código de moeda existente!")
else:
  print(f"Falha na requisição! Código de erro: {response.status_code}")
