print("** SISTEMA DE RESERVAS **")

# constantes
QTO_SEM_VISTA = 150.50
QTO_COM_VISTA = 190.50

# entrada de dados
nome = input("Qual o seu nome?: ").strip().title()
estadia = int(input("Qual seu tempo de estadia?: "))
vista_mar = input("Tem vista para o mar (Sim/Nao): ").strip().lower()

# conversão para boolean
tem_vista = vista_mar == "sim"

# cálculo
valor_estadia = QTO_COM_VISTA if tem_vista else QTO_SEM_VISTA
valor_total = valor_estadia * estadia

# saída
print(f"\nOlá {nome}!")
print(f"Estadia: {estadia} dias")
print(f"Possui vista para o mar? {'Sim' if tem_vista else 'Não'}")
print(f"Valor total: R$ {valor_total:.2f}")
