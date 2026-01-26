print("** SISTEMA DE VENDAA. **")

#enntrada de dados
preco_arroz = float(input("Preco do arroz: "))
preco_feijao = float(input("Preco do feijao: "))
preco_frango = float(input("Preco do frango: "))
imposto = float(input("Imposto: "))
desconto = float(input("Aplique em % o desconto que deve ser aplicado: "))

#subtotal
subtotal = preco_arroz + preco_feijao + preco_frango

#imposto
valor_imposto = subtotal * (imposto / 100)

#desconto
valor_desconto = subtotal * (desconto / 100)

#preco total
total = subtotal + valor_imposto - valor_desconto

texto = f"""
Subtotal: R${subtotal:.2f}
Desconto ({desconto:.1f}%): R${valor_desconto:.2f}
Imposto ({imposto:.1f}%): R${valor_imposto:.2f}
Custo total da compra: R${total:.2f}
"""
print(texto)


