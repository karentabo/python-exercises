agenda = [
    {
        'nome': 'Alexandre',
        'sobrenome': 'Pires',
        'idade': 18
    },
    {
        'nome': 'Carla',
        'sobrenome': 'Perez',
        'idade': 25
    }
]

#imprimindo os nomes
print(f'''Nome: {agenda[0]['nome']}
Sobrenome: {agenda[0]['sobrenome']}
Idade: {agenda[0]['idade']}''')

for contador, agenda in enumerate(agenda):
    print(f'{contador + 1}: {agenda}')
    #print(f'Nome: {agenda['nome']}')
    #print(f'Sobrenome: {agenda['sobrenome']}')
    #print(f'Idade: {agenda['idade']}')
