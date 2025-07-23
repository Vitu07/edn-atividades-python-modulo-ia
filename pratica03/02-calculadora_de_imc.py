"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""


peso = float(input("Infrome seu peso: "))
altura = float(input("Informe sua altura: "))
imc = peso/altura**2

if imc < 18.5:
    print(f"Seu imc é {imc:.2f}, você está abaixo do peso")
elif imc < 25:
    print(f"Seu imc é {imc:.2f}, você está com o peso ideal")
elif imc < 30:
    print(f"Seu imc é {imc:.2f}, você está com sobrepeso")
else:
    print(f"Seu imc é {imc:.2f}, você está obeso")
