"""
1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.
"""

try:
  primeiro_numero = float(input("Digite o primeiro número: "))
  segundo_numero = float(input("Digite o segundo número: "))
  resultado =0
  while True:
    operacao = str(input("Informe a operação que deseja: "))
    if operacao == "+":
      resultado = primeiro_numero + segundo_numero
      break
    elif operacao == "-":
      resultado = primeiro_numero - segundo_numero
      break
    elif operacao == "*":
      resultado = primeiro_numero * segundo_numero
      break
    elif operacao == "/":
      resultado = primeiro_numero/segundo_numero
      break
    else:
      print("Operação não suportada, por favor informe uma operação válida! ('+', '-', '*' ou '/')")
  print(f"{primeiro_numero} {operacao} {segundo_numero} = {resultado:.2f}")

except ValueError:
  print("Por favor, informe apenas valores numéricos")
except ZeroDivisionError:
  print("ERRO! Não é possível realizar divisão por zero")
