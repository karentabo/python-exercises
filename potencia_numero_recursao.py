print('** POTENCIA DE UM NUMERO **')

def potencia(base, expoente):
    if expoente == 0: #caso base
        return 1
    return base * potencia(base, expoente - 1) #caso recursivo

print(potencia(4,3))

#metodo for

base = 4
expoente = 3
resultado = 1

for _ in range(expoente):
    resultado *= base

print(resultado)