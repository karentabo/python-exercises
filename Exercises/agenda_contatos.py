print('** AGENDA DE CONTATOS **')

agenda = {
    'Raisa': {
        'Telefone': 55666775,
        'Email': 'raisa@gmail.com',
        'Endereco': 'Rua 2',
    }
}

nome = input('Digite o nome do contato: ').strip().title()

agenda[nome] = {
    'Telefone': input('Digite o telefone: ').strip(),
    'Email': input('Digite o email: ').strip().lower(),
    'Endereco': input('Digite o endereco: ')
}

print('\nAgenda atual:')
for contato, dados in agenda.items():
    print(f'\nNome: {contato}')
    for chave, valor in dados.items():
        print(f'  {chave}: {valor}')


