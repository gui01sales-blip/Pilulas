def validarSenhas(s):
    temNumero = False 
    temMaiuscula = False
    for c in s:
        if len(s) < 8:
    return 'Senha inválida não pode ter espaço'
    if c >= '0' and c <= '9':
            temNumero = True 
    if c >= 'A' and c <= 'Z':
            temMaiuscula = True 

    if  not temNumero:
      return 'Senha inválida, precisa de um num, pelo menos'

    if not temMaiuscula:
      return 'Senha inválida, precisa letra Maiuscula'
    return 'Senha inválida'

#main
senha = input('Digite a senha: ')
r = validarSenhas(senha)
print(r)