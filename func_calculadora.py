print('** CALCULADORA **')

def menu():
    print('\nEscolha uma operacao a ser feita:')
    print('1 - Soma')
    print('2 - Subtracao')
    print('3 - Multiplicacao')
    print('4 - Divisao')
    print('5 - Exponencao')
    print('6 - Sair')
    return int(input('Digite sua opcao: '))

def pedir_valores():
    operador1 = int(input('Digite o primeiro valor: '))
    operador2 = int(input('Digite o segundo valor: '))
    return operador1, operador2

def executar_operacao(opcao, sair):
    if 1 <= opcao <= 5:
        operador1, operador2 = pedir_valores()

        if opcao == 1:
            print(f'Soma de {operador1} + {operador2} = {soma(operador1, operador2)}')
        elif opcao == 2:
            print(f'Subtracao de {operador1} - {operador2} = {subtracao(operador1, operador2)}')
        elif opcao == 3:
            print(f'Multiplicacao de {operador1} * {operador2} = {multiplicacao(operador1, operador2)}')
        elif opcao == 4:
            print(f'Divisao de {operador1} / {operador2} = {divisao(operador1, operador2):.2f}')
        elif opcao == 5:
            print(f'Exponencao de {operador1} elevado a {operador2} = {exponencao(operador1, operador2)}')
    elif opcao == 6:
        print('Saindo da calculadora...')
        sair = True
    else:
        print('!--- Opcao invalida ---!')

    return sair

def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a * b
def divisao(a,b):
    return a / b

def exponencao(a,b):
    return a ** b

def sair():
    print('Saindo...')

if __name__ == '__main__':
    sair = False
    while not sair:
        opcao = menu()
        sair = executar_operacao(opcao, sair)