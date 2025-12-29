print('** CALCULADORA **')

while True:
    print('''
Escolha um tipo de calculo:
    1. Somar
    2. Subtrair
    3. Multiplicar
    4. Dividir
    5. Sair
''')

    opcao = int(input('Qual a sua opcao? '))

    if opcao == 5:
        print('Saindo do sistema...')
        break

    if opcao not in [1, 2, 3, 4]:
        print('Opcao invalida!')
        continue

    x = float(input('Digite o primeiro valor: '))
    y = float(input('Digite o segundo valor: '))

    if opcao == 1:
        resultado = x + y
        tipo = 'soma'
    elif opcao == 2:
        resultado = x - y
        tipo = 'subtracao'
    elif opcao == 3:
        resultado = x * y
        tipo = 'multiplicacao'
    elif opcao == 4:
        if x == 0 or y == 0:
            print('Nao e possivel dividir por zero!')
            continue
        resultado = x / y
        tipo = 'divisao'

    print(f'O resultado da sua {tipo} eh: {resultado:.2f}')
