"""
3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""

def calculadora_de_desconto(preco_produto, porcentagem_desconto):
  valor_de_desconto = preco_produto * (porcentagem_desconto/100)
  return preco_produto - valor_de_desconto

try:
  preco_produto = float(input("Insira o valor do produto:\n"))
  porcentagem_desconto = float(input("Insira a porcentagem de desconto:\n"))
except ValueError:
  print("Insira apenas valores númericos!")

resultado_funcao = calculadora_de_desconto(preco_produto, porcentagem_desconto)
print(f"O preço final com o desconto aplicado é de: {resultado_funcao:.2f}")
  