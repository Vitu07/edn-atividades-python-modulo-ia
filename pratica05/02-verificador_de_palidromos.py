"""
2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.
"""
import re
import unicodedata

def verificar_palidromos(texto_original): 
  texto_ao_contrario = texto_original[::-1].lower()
  texto_ao_contrario = re.sub(r'[^\w]', '', texto_ao_contrario)
  texto_ao_contrario = removerAcentos(texto_ao_contrario)

  texto_original = re.sub(r'[^\w]', '', texto_original).lower()
  texto_original = removerAcentos(texto_original)

  é_palindromo = texto_original == texto_ao_contrario

  if é_palindromo:
    return "Sim"
  else: 
    return "Não"

def removerAcentos(texto):
  texto = unicodedata.normalize('NFD', texto)
  texto = texto.encode('ascii', 'ignore')
  texto = texto.decode("utf-8")
  return texto

frase_ou_palavra = input("Informe uma frase ou palavra para verificar se é um um palindromo: ")
resultado_da_funcao = verificar_palidromos(frase_ou_palavra)
print(f"O texto é palidromo?\n{resultado_da_funcao}")