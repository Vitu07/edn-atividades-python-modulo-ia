"""
1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.
"""
import random
import string

tamanho_senha = int(input("Informe o tamanho de sua senha(8, 12 ou 16): "))

todos_caracteres = string.printable
letras_maiusculas = string.ascii_uppercase
letras_minusculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

senha_segura = []
senha = ""


for i in range(0, tamanho_senha, 1):  
  senha_segura.append(random.choice(todos_caracteres))

if not any(c in letras_maiusculas for c in senha_segura):
  senha_segura[random.randint(0, len(senha_segura))] = random.choices(letras_maiusculas)
if not any(c in letras_minusculas for c in senha_segura):
  senha_segura[random.randint(0, len(senha_segura))] = random.choices(letras_minusculas)
if not any(c in numeros for c in senha_segura):
  senha_segura[random.randint(0, len(senha_segura))] = random.choices(numeros)
if not any(c in simbolos for c in senha_segura):
  senha_segura[random.randint(0, len(senha_segura))] = random.choices(simbolos)

for c in senha_segura:
  senha = senha + c

print(f"Sua senha forte é: {senha}")
