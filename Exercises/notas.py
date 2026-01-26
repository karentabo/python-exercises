print("** SISTEMA DE NOTAS **")

nota = int(input("Digite a nota do aluno entre 0 e 10: "))

#atribuicao da nota numerica por letra

nota_final = None

if nota < 0 or nota > 10:
    print("Digite uma nota valida entre 0 e 10.")
else:
    if 9 <= nota <= 10:
        nota_final = "A"
    elif 8 <= nota < 9:
        nota_final = "B"
    elif 7 <= nota < 8:
        nota_final = "C"
    elif 6 <= nota < 7:
        nota_final = "D"
    elif 0 <= nota < 6:
        nota_final = "F"

    print(f"A nota {nota} eh um {nota_final}!")