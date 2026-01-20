print('** CALCULADORA DE IMPOSTO **')

def valores():
    valor_produto = float(input('Qual o valor do produto: '))
    valor_imposto = float(input('Qual o valor do imposto: '))
    return valor_produto, valor_imposto

def calculo(valor_produto, valor_imposto):
    valor_total = valor_produto + valor_produto * (valor_imposto/100)
    return valor_total

if __name__ == '__main__':
    valor_produto, valor_imposto = valores()
    total = calculo(valor_produto, valor_imposto)
    print(f'O valor total do produto + imposto = {total}')