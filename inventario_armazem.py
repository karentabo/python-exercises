print('** Gestao de armazenamento **')

estoque = []

numero_produtos = int(input('Quantos produtos deseja adicionar?: '))

for i in range(numero_produtos):
    print(f'Proporcione os valores do {i+1}o produto:')
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preco do produto: '))
    qtd = int(input('Digite quantos itens em estoque: '))
    #criando um dicionario para adicionar as informacoes
    produto = {'id': i + 1, 'nome': nome, 'preco': preco, 'qtd': qtd}
    #adicionado a uma lista
    estoque.append(produto)

#impressao do estoque atual
print(' --- ESTOQUE ---')
for produto in estoque:
    print(f'''ID: {produto['id']}
Nome: {produto['nome'].title()}
Preco: {produto['preco']}
Quantidade: {produto['qtd']}
''')

#procurar um produto
procurar_id = int(input('Digite o id do produto que voce deseja buscar: '))
produto_encontrado = None
for produto in estoque:
    if produto['id'] == procurar_id:
        produto_encontrado = produto
        break

if produto_encontrado is not None:
    print('\n** PRODUTO ENCONTRADO **')
    print(f'''Id: {produto_encontrado['id']}
Nome: {produto_encontrado['nome']}
preco: R${produto_encontrado['preco']:.2f}
qtd: {produto_encontrado['qtd']}
''')
else:
    print(f'Produto com o ID {procurar_id} nao encontrado')