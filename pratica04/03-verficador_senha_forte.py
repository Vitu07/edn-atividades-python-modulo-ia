"""
3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".
"""

senha_forte = False
verficar_tamanho_minimo_senha = False
verficar_senha_contem_numero = False
tamanho_minimo_senha = 8

while senha_forte != True:
  senha = input("Informe uma senha:\n")

  if len(senha) >= tamanho_minimo_senha : verficar_tamanho_minimo_senha = True

  for char in senha:
    if char.isnumeric(): verficar_senha_contem_numero = True

  if(verficar_tamanho_minimo_senha and verficar_senha_contem_numero): 
    print("Sua senha é forte")
    senha_forte = True
  else:
    print("Sua senha é fraca")
    print("CONTINUAR - continue o programa")
    controle_programa = input("SAIR - encerra o programa\n").lower()
    if controle_programa == "sair": break


  