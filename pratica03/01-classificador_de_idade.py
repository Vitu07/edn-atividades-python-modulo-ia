"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).
"""

idade = int(input("Informe sua idade: "))

if idade >= 60:
    print(f"Sua idade é {idade}, você é um idoso")
elif idade >= 18:
    print(f"Sua idade é {idade}, você é um adulto")
elif idade >= 13:
    print(f"Sua idade é {idade}, você é um adolescente")
else:
    print(f"Sua idade é {idade}, você é uma criança")