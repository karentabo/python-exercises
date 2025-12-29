print("** ENCONTRAR O MAIOR NUMERO **")

print("Digite dois numeros:")
numero1 = int(input())
numero2 = int(input())

maior = numero1 if numero1 > numero2 else numero2

print(f"O maior numero entre {numero1} e {numero2} eh: {maior}")