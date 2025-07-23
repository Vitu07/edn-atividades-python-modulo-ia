"""
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

ano = int(input("Informe o ano que deseja descobrir se é bissexto: "))
verificar_ano_bissexto = bool((ano % 4 ==0 and ano % 100 !=0) or (ano % 100 == 0 and ano % 400 ==0))

if verificar_ano_bissexto :
    print(f"O ano {ano}, é bissexto")
else:
    print(f"O ano {ano}, não é bissexto")
