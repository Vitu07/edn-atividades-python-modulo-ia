"""4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. 
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final."""

nome_do_produto = "Cadeira Infantil"
preco_do_produto = 12.4
quantidade_do_produto = 3

preco_total_do_produto = preco_do_produto * quantidade_do_produto

print(f"Nome do produto: {nome_do_produto}")
print(f"Preço unitario do produto: {preco_do_produto:.2f}")
print(f"quantidade do poduto: {quantidade_do_produto}")
print(f"Preço total do produto: {preco_total_do_produto}")