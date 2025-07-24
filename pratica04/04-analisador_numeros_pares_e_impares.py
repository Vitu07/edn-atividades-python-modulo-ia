"""
4- Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.
"""
contador_numeros_pares = 0
contador_numeros_impares = 0

while(True):
  try:
    numero = int(input("Informe um número: "))

    if numero % 2 == 0:
      print(f"O numero {numero} é par")
      contador_numeros_pares = contador_numeros_impares + 1
    else: 
      print(f"O número é {numero} impar")
      contador_numeros_impares = contador_numeros_impares + 1

    controle_programa = input("FIM - encerrar o programa\n").lower()
    if controle_programa == "fim": break
  except ValueError:
    print("Informe apenas números!")

print(f"Quantidade de números pares: {contador_numeros_pares}")
print(f"Quantidade de números impares: {contador_numeros_impares}")