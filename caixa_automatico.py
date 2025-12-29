print("** CAIXA AUTOMATICO **")

saldo = 1000.00
sair = False

while not sair:
    print("""
Escolha uma das operacoes abaixo:
    1. Consultar saldo
    2. Saque
    3. Deposito
    4. Sair """)

    opcao = int(input("Escolha uma das operacoes: "))

    if opcao == 1:
        print(f"Seu saldo atual eh: ${saldo:.2f}")

    elif opcao == 2:
        saque = 0
        print(f"Seu saldo atual eh de {saldo:.2f}")
        saque = float(input("Qual o valor que voce deseja sacar?: "))

        if saque > saldo:
            print(f"Este valor eh maior que seu saldo de ${saldo:.2f}")
        elif saque < saldo:
            saldo -= saque
            print(f"Voce sacou ${saque:.2f}. Saldo atual: ${saldo:.2f}")

    elif opcao == 3:
        deposito = 0.00
        deposito = float(input("Qual valor deseja depositar?: "))
        saldo += deposito
        print(f"Seu saldo atual eh: ${saldo:.2f}")

    elif opcao == 4:
        sair = True
        print("Saindo do sistema...")
        print("Aplicacao finalizada!")

    else:
            print("Opcao invalida. Tente novamente.")