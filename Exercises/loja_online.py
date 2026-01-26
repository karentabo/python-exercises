print("** LOJA ONLINE **")

valor_compra = float(input("Qual o valor da compra?: "))
membro = input("O cliente eh membro? (s/n): ").strip().lower()

#definir valor do desconto
desconto = 0

if valor_compra >= 1000 and membro == "s":
    desconto = 0.10
elif valor_compra < 1000 and membro == "s":
    desconto = 0.05

#definir saida
valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

if desconto != 0:
    print(f"""
        Parabens! Voce ganhou {desconto * 100:.0f}% de desconto.
        Valor da compra: R$ {valor_compra:.2f}
        Valor do desconto: R$ {valor_desconto:.2f}
        Total a pagar: R${valor_final:.2f}
    """)
else:
    print(f"""
        Voce nao obteve desconto. Seja um membro para adquirir beneficios.
        Valor da compra: R$ {valor_compra:.2f}
        Valor do desconto: R$ {valor_desconto:.2f}
        Total a pagar: R${valor_final:.2f}
    """)
