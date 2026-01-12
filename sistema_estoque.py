print('** SISTEMA DE ESTOQUE **')

#estoque do armazem
estoque = [
    {'id': 1, 'nome': 'Arroz', 'preco': 3.00, 'qtd': 2},
    {'id': 2, 'nome': 'Feijao', 'preco': 5.00, 'qtd': 2},
    {'id': 3, 'nome': 'Carne', 'preco': 40.00, 'qtd': 2},
]

#funcao para mostrar o estoque
def mostrar_estoque():
    print('\n** Estoque do armazem **')
    for produto in estoque:
        print(f'Id: {produto['id']} - Nome: {produto['nome']}; Preco: ${produto['preco']:.2f}; Quantidade: {produto['qtd']} ')

def adicionar_item():
    print('\n** Adicionar item ao estoque **')
    novo_id = len(estoque) + 1
    nome = input('Digite o nome do produto: ').strip().title()
    preco = float(input('Digite o preco do produto: '))
    qtd = int(input('Digite a quantidade do produto: '))

    novo_produto = {'id': novo_id, 'nome': nome, 'preco': preco, 'qtd': qtd}
    estoque.append(novo_produto)
    print('Produto adicionado com sucesso!')
    print(f'Id: {novo_id} - Nome: {nome}; Preco: ${preco:.2f}; Quantidade: {qtd} ')


def buscar_item_id():
    print('\n** Buscar item no estoque **')
    buscar_id = int(input('Digite o ID do produto: '))

    for produto in estoque:
        if produto['id'] == buscar_id:
            print(f"Id: {produto['id']} - Nome: {produto['nome']}; Preco: ${produto['preco']:.2f}; Quantidade: {produto['qtd']}")
            return

    print('Produto nao localizado')


# programa (menu)
if __name__ == '__main__':
    while True:
        print('\n -- Menu --')
        print('1. Mostrar estoque')
        print('2. Adicionar item ao estoque')
        print('3. Buscar um item ao estoque')
        print('4. Sair')
        opcao = input('\nDigite sua opcao: ')

#Revisando o input do menu
        if opcao == '1':
            mostrar_estoque()
        elif opcao == '2':
            adicionar_item()
        elif opcao == '3':
            buscar_item_id()
        elif opcao == '4':
            print('Saindo do sistema...')
            break
        else:
            print('Opcao invalida. Proporcione uma opcao valida!')





