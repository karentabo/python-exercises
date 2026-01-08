print('** FATORIAL **')

def fatorial(numero):
    if numero == 0 or numero == 1:
        print(f'Resultado fatorial parcial {numero} = 1')
        return 1
    else:
        fatorial_parcial = numero * fatorial(numero - 1)
        print(f'Resultado fatorial parcial {numero} = {fatorial_parcial}')
        return fatorial_parcial

numero = 5
resultado = fatorial(numero)
print(f'Resultado fatorial de {numero} = {resultado}')


print('** FATORIAL **')

numero = 5
resultado = 1

for i in range(1, numero + 1):
    resultado *= i
    print(f'Resultado fatorial parcial de {i} = {resultado}')

print(f'Resultado fatorial de {numero} = {resultado}')


