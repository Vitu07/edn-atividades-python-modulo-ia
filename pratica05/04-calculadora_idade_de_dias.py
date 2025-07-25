"""
4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.
"""

def calculadora_idade_dia(ano_nascimento, ano_atual):
  idade = ano_atual - ano_nascimento
  idade_em_dias = idade * 365
  return idade_em_dias

try:
  ano_de_nascimento = int(input("Informe seu ano de nascimento:\n"))
  resultado_da_funcao = calculadora_idade_dia(ano_de_nascimento, ano_atual=2025)
  print(f"A sua idade aproximada convertida em dias é: {resultado_da_funcao}")
except ValueError:
  print("Informe apenas numero!")