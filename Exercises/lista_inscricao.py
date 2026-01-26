print('** LISTA DE INSCRITOS **')

inscritos = set()

#validacao de quantidade
while True:
    numero_inscritos = int(input('Quantos incritos deseja adicionar? (De 1 a 3): '))
    if 1 <= numero_inscritos <= 3:
        break
    else:
        print('Valor invalido')

# cadastro dos e-mails
for i in range(numero_inscritos):
    email = input(f'Digite o {i + 1}º e-mail: ').strip().lower()

    if email in inscritos:
        print(f'O e-mail {email} já está cadastrado.')
    else:
        inscritos.add(email)
        print(f'E-mail {email} adicionado com sucesso!\n')

#total de inscritos
print(f'Voce tem um total de {len(inscritos)} inscritos.')

#lista de incritos
print('\n-- Lista de inscritos --')
for inscrito in inscritos:
    print(f'- {inscrito}')

#remover um inscrito
#remover_inscrito = input('Digite seu e-mail: ').strip().lower()
#inscritos.remove(remover_inscrito)
