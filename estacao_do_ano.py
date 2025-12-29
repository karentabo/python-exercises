print("** Identificar a estacao do ano **")

mes = int(input("Digite qual a mes do ano de 1 a 12: "))

#definicao dos meses para atribuir a estacao do ano

estacao = None

if mes == 1 or mes == 2 or mes == 12:
    estacao = "Inverno"
elif mes == 3 or mes == 4 or mes == 5:
    estacao = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacao = "Verao"
elif mes == 9 or mes == 10 or mes == 11:
    estacao = "Outono"
else:
    estacao = "Digite o mes entre 1 e 12 para saber a estacao do ano"

print(f"A estacao do mes {mes} eh: {estacao}")
