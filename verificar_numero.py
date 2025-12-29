VALOR_MINIMO = 0
VALOR_MAXIMO = 5

x = int(input(f"Digite um valor de {VALOR_MINIMO} a {VALOR_MAXIMO}: "))

#Verificar se esta dentro dos valores
dentro_range = VALOR_MINIMO <= x <= VALOR_MAXIMO
print(dentro_range)

