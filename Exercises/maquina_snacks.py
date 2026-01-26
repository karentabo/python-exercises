print('** MAQUINA DE SNACKS **')

snacks = [
    {'id': 1, 'nome': 'Chocolate', 'preco': 2.00, 'qtd': 2 },
    {'id': 2, 'nome': 'Bala', 'preco': 0.50, 'qtd': 3 },
    {'id': 3, 'nome': 'Chiclete', 'preco': 1.50, 'qtd': 1 },
]

item_comprado = []

def buscar_snack_por_id(id_buscar):
    for produto in snacks:
        if produto['id'] == id_buscar:
            return produto
    return None

def comprar_snack():
    compra = int(input('Qual o ID do produto que deseja comprar?: '))
    snack_encontrado = buscar_snack_por_id(compra)

    if snack_encontrado is None:
        print(f'Produto nao localizado com ID {compra}')
        return

    if snack_encontrado['qtd'] <= 0:
        print(f'O ID {snack_encontrado["id"]} -> ({snack_encontrado["nome"]}) nao esta mais disponivel')
        return

    snack_encontrado['qtd'] -= 1

    item_comprado.append({
        'id': snack_encontrado['id'],
        'nome': snack_encontrado['nome'],
        'preco': snack_encontrado['preco'],
        'qtd': 1
    })

    print(f'Produto {snack_encontrado["id"]} -> {snack_encontrado["nome"]} comprado com sucesso!')

def ver_estoque():
    print('-- ESTOQUE --')
    for produto in snacks:
        print(f'ID: {produto["id"]} - Nome: {produto["nome"]}, '
              f'- Preco: ${produto["preco"]:.2f} - Quantidade: {produto["qtd"]}')

def ver_compra(item_comprado):
    if len(item_comprado) == 0:
        print('Nenhum item comprado ainda.')
        return

    print('-- Itens comprados --')

    total = 0
    for produto in item_comprado:
        subtotal = produto['preco'] * produto['qtd']
        total += subtotal

        print(f'{produto["nome"]} x{produto["qtd"]} - ${subtotal:.2f}')

    print('----------------------')
    print(f'Total da compra: ${total:.2f}')

def pagamento(item_comprado):
    if len(item_comprado) == 0:
        print('Nenhum item foi comprado!')
        return

    finalizar_compra = input('Deseja finalizar a compra? [S/N]: ').strip().lower()
    if finalizar_compra == 'n':
        return

    total = 0
    for produto in item_comprado:
        total += produto['preco']

    print(f'Valor total da compra: ${total:.2f}')

def sair():
    print('Saindo...')

if __name__ == '__main__':
    while True:
        print('\n-- Selecione uma das opcoes --')
        print('1. Comprar snack')
        print('2. Ver estoque')
        print('3. Ver items comprados')
        print('4. Efetuar o pagamento')
        print('5. Sair')
        opcao = input('Digite uma opcao: ')

        if opcao == '1':
            comprar_snack()
        elif opcao == '2':
            ver_estoque()
        elif opcao == '3':
            ver_compra(item_comprado)
        elif opcao == '4':
            pagamento(item_comprado)
        elif opcao == '5':
            sair()
            break
        else:
            print('Opcao invalida! Digite novamente!')
