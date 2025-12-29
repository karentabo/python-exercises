print('** DESENHANDO TRIANGULO **')

num_linhas = int(input('Digite o numero de linhas do seu triangulo: '))

print('\n** TRIANGULO **\n')
for linhas in range(1, num_linhas + 1):
    espaco_branco = ' ' * (num_linhas - linhas)
    asterisco = '*' * (2 * linhas - 1)
    print(f'{espaco_branco}{asterisco}')

print('\n** TRIANGULO INVERTIDO **\n')

for linha in range(num_linhas, 0, -1):
    espaco_branco = ' ' * (num_linhas - linha)
    asteriscos = '*' * (2 * linha - 1)
    print(f'{espaco_branco}{asteriscos}')