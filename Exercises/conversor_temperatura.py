print('** CONVERSOR DE TEMPERATURA **')

def pedir_temperatura():
    temp = float(input('Informe a temperatura: '))
    return temp

def fahrenheit_para_celsius(temperatura):
    conversao = (temperatura - 32) / 1.8
    return conversao

def celsius_para_fahrenheit(temperatura):
    conversao = temperatura * 1.8 + 32
    return conversao


def menu():
    print('1. Converter Fahrenheit para Celsius')
    print('2. Converter Celsius para Fahrenheit')

    opcao = int(input('Qual a opcao? '))
    if opcao == 1:
        temp = pedir_temperatura()
        resultado = fahrenheit_para_celsius(temp)
        print(f'Resultado: {resultado:.2f} °C')
    elif opcao == 2:
        temp = pedir_temperatura()
        resultado = celsius_para_fahrenheit(temp)
        print(f'Resultado: {resultado:.2f} °F')
    else:
        print('Opcao invalida!')

menu()