"""
1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.
"""

def calculo_de_gorjeta(valor_conta, porcentagem_gorjeta):
  return valor_conta * porcentagem_gorjeta/100

try:
  valor_conta = float(input("Insira o valor total da conta:\n"))
  porcentagem_gorjeta = float(input("Informe a porcentagem de gorjeta:\n"))
except ValueError:
    print("Insira apenas valores numérico!")
    
resultado_funcao = calculo_de_gorjeta(valor_conta, porcentagem_gorjeta) 
print(f"O valor da gorjeta é: {resultado_funcao:.2f}")
