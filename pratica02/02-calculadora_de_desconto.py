"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_produto = "Camiseta"
preco_padrao = 50
porcentagem_desconto = 20
valor_desconto = 50 * porcentagem_desconto/100

print(f"Nome do produto: {nome_produto}")
print(f"Preço original: R$ {preco_padrao:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: {valor_desconto:.2f}")