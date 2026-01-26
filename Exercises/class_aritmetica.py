print('--- CALCULADORA ---')

def menu():
    print('Selecione a operacao a ser realizada:')
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Sair')
    opcao = input('Digite a opcao desejada: ')
    return opcao

def pedir_entrada():
    operador1 = int(input('Proporcione o primeiro operador: '))
    operador2 = int(input('Proporcione o segundo operador: '))
    return operador1, operador2

class Calculadora:
    def __init__(self, operador1, operador2):
        self._operador1 = operador1
        self._operador2 = operador2

    def soma(self):
        return self._operador1 + self._operador2
    def subtracao(self):
        return self._operador1 - self._operador2

    @property
    def operador1(self):
        return self._operador1

    @property
    def operador2(self):
        return self._operador2

    @operador1.setter
    def operador1(self, operador):
        self._operador1 = operador

    @operador2.setter
    def operador2(self, operador):
        self._operador2 = operador

if __name__ == '__main__':
    while True:
        opcao = menu()

        if opcao == '1':
            operador1, operador2 = pedir_entrada()
            calc = Calculadora(operador1, operador2)
            resultado = calc.soma()
            print(f'A soma de {operador1} + {operador2} = {resultado}')
        elif opcao == '2':
            operador1, operador2 = pedir_entrada()
            calc = Calculadora(operador1, operador2)
            resultado = calc.subtracao()
            print(f'A subtracao de {operador1} - {operador2} = {resultado}')
        elif opcao == '3':
            print('Saindo do programa')
            break
        else:
            print('Opcao invalida!\n')