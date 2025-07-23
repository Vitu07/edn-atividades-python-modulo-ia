"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temperatura = float(input("Infrome a temperatura: "))
temperatura_convertida = 0

print("""
C - Celsius
F - Fahrenheit   
K - Kelvin
""")

unidade_temperatura_origem = str.upper(input("Infrome a unidade de medida temperatura origem: "))
unidade_temperatura_desejada = str.upper(input("Informe a unidade de medida da temperatura que deseja converter: "))

if unidade_temperatura_origem == "C" and unidade_temperatura_desejada == "F":
    temperatura_convertida = temperatura * 1.8 + 32
elif unidade_temperatura_origem == "F" and unidade_temperatura_desejada == "C":
    temperatura_convertida = (temperatura - 32)/1.8
elif unidade_temperatura_origem == "K" and unidade_temperatura_desejada == "F":
    temperatura_convertida = temperatura_convertida = (temperatura * 9/5) - 459.67
elif unidade_temperatura_origem == "F" and unidade_temperatura_desejada == "K":
    temperatura_convertida = (temperatura + 459.67) * 5/9
elif unidade_temperatura_origem == "C" and unidade_temperatura_desejada == "K":
    temperatura_convertida = temperatura + 273.15
elif unidade_temperatura_origem == "K" and unidade_temperatura_desejada == "C":
    temperatura_convertida = temperatura - 273.15
else:
    print("Conversão inválida")
    exit()

print(f"A temperatura convertida fica {temperatura_convertida:.0f}°{unidade_temperatura_desejada}")
