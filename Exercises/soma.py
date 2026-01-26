MAXIMO = 5
cont = 1
soma = 0

print(f"Valor parcial da soma: ", end="")
while cont <= MAXIMO:
    soma += cont
    print(soma, end=" ")
    cont += 1

print(f"\nResultado acumulado: {soma}")