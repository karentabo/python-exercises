print("** SISTEMA DE DESCONTOS VIP **")

#entrada de dados
produtos_comprados = int(input("Quantos produtos foram comprados?: "))
membro_loja = input("O cliente e membro da loja? (S/N): ")

#avaliar se o cliente tem beneficios
if produtos_comprados >= 10 and membro_loja.strip().lower() == "s":
    print("Parabens, seu desconto foi concedido.")
elif produtos_comprados < 10 and membro_loja == "s" :
    print("Voce precisa comprar 10 itens para ganhar o desconto.")
else:
    print("Voce nao e membro, e portanto nao e elegivel para desconto.")