print('** VALIDACAO DE SENHA **')

while True:
    senha = input('Digite sua senha: ').strip()

    if len(senha) >= 6:
        print('Senha criada com sucesso!')
        break
    else:
        print('Sua senha deve conter ao menos 6 caracteres')