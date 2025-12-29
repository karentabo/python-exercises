from random import randint

print('** ADIVINHE O NUMERO **')

MAX_TENTATIVA = 5

opcao = input('Deseja iniciar o jogo? (s/n): ').strip().lower()

while opcao not in ('s', 'n'):
    opcao = input('Opcao invalida. Deseja iniciar? (s/n): ').strip().lower()

if opcao == 's':
    print('** SORTEANDO O NUMERO **')
    print(f'Lembre-se que voce apenas tem {MAX_TENTATIVA} tentativas.')
    num_aleatorio = randint(1, 10)

    tentativas = 0
    while True and tentativas < MAX_TENTATIVA:
        tentativas += 1
        num_escolhido = int(input(f'Digite um numero entre 1 e 10): '))

        if num_escolhido < 1 or num_escolhido > 10:
            print('Numero fora do intervalo!')
        elif num_escolhido != num_aleatorio:
            print('** Numero incorreto!**', end=' ')
            if num_escolhido > num_aleatorio:
                print("O numero eh menor que o escolhido.")
            else:
                print("O numero eh maior que o escolhido.")
        else:
            print(f'Parabens! O numero {num_aleatorio} esta correto! Voce acertou em {tentativas} tentativas.')
            break

        print(f'Numero de tentativas: {tentativas}')

    else:
        print('O numero de tentativas foi esgotado!')

