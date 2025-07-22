"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

distancia_percorrida = 300
quantidade_combustivel_gasto = 25
consumo_medio = distancia_percorrida/quantidade_combustivel_gasto


print(f"Distancia percorrida(em KM): {quantidade_combustivel_gasto}")
print(f"Quantidade de combustivel gasto(em litros): {quantidade_combustivel_gasto}")
print(f"Consumo médio: {consumo_medio:.2f}")