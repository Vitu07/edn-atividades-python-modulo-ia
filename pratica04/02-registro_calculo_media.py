"""
2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.
"""

notas = []
notas = (notas)
notas_validas = 0
media = 0


controle_de_notas = "sim"
while controle_de_notas == "sim":
  try:
    nota = float(input("Informe a nota que deseja armazenar: "))
    
    if nota < 0 or nota > 10: 
      print("Informe uma nota válida! (valor entre  0 e 10)")
      continue

    notas.append(nota)
    notas_validas = notas_validas + 1

    controle_de_notas = input("Deseja continuar? \n").lower()
    
  except ValueError:
    print("Informe apenas número!")

for nota in notas:
  media = media + nota

media = media/len(notas)

print(f"A média da turma é: {media:.2f}")
print(f"Quantidade de notas válidas registradas: {notas_validas}")