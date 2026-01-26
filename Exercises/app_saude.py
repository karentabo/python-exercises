print("** APP SAUDE E FITNESS **")

#constantes
META_POR_PASSO = 10000
CALORIAS_POR_PASSO = 0.04 #valor aproximado de queima de calorias

#entrada de dados
nome = input("Qual o seu nome?: ").strip().capitalize()
passos_diarios = int(input("Quantos passos no dia?: "))

#saudacao
print(f"Ola {nome}!!")

#calculo de queima de calorias
calorias_queimadas = passos_diarios * CALORIAS_POR_PASSO
print(f"Caloria queimadas: {calorias_queimadas:.0f}")

#verificar se meta diaria foi alcancada
meta_alcancada = "Sim" if passos_diarios >= META_POR_PASSO else "Nao"
print(f"Meta de passo diaria atingida?: {meta_alcancada}")
