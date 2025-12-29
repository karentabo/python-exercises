print("** CALCULO DE FRETE **")

#CUSTOS DAS TARIFAS - CONSTANTES
NACIONAL = 10 #reais por kilo
INTERNACIONAL = 20 #reais por kilo

#inputs
destino = input("Digite se o destino eh nacional ou internacional: ").strip().lower()
peso = float(input("Qual o peso do seu pacote em kilos?: ").strip())

#calculo de envio
valor_final = 0.0

if destino == "nacional":
    valor_final = peso * NACIONAL
elif destino == "internacional":
    valor_final = peso * INTERNACIONAL
else:
    print("Coloque um destino valido (nacional/internacional)")

#output
if valor_final != 0.0:
    print(f"Seu destino eh {destino}, e o valor de envio eh {valor_final:.2f}")