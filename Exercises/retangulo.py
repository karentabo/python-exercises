print("**CALCULO DE AREA E PERIMETRO DE UM RETANGULO**")

#Entrada de dados
base = float(input("Digite a base do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

#Calculo da base
area = base * altura
perimetro = 2 * (base + altura)

#visualizacao
print(f"A area do retangulo eh de {area:.1f}")
print(f"O perimetro do retangulo eh de {perimetro:.1f}")
