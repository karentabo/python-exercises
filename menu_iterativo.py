print("** SISTEMA DE ADMINISTRAÇÃO DE CONTAS **")

sair = False

while not sair:
    print("""
    Menu:
    1. Criar conta
    2. Excluir conta
    3. Sair
    """)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\nCriando a conta...")
    elif opcao == 2:
        print("\nExcluindo a conta...")
    elif opcao == 3:
        print("\nSaindo do sistema...")
        sair = True
    else:
        print("\nOpção inválida.")