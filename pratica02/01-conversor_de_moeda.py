"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

valor_em_reais = 100
taxa_dolar = 5.20
taxa_euro = 6.15

conversao_para_dolar = valor_em_reais/taxa_dolar
conversao_para_euro = valor_em_reais/taxa_euro

print(f"A conversão de R$ {valor_em_reais:.2f} fica € {conversao_para_euro:.2f}")
print(f"A conversão de R$ {valor_em_reais:.2f} fica $ {conversao_para_dolar:.2f}")