"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

notas = [7.5, 8, 6.5]
media = 0

for i in range(0, len(notas), 1):
  print(notas[i])
  media += notas[i]

media/len(notas)

print(f"A média é: {media:.2f}")
 