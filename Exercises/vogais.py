print('** ENCONTRAR VOGAIS **')

texto = 'Ola mundo'.lower()

cont = 0

for vogais in texto:
    if vogais in 'aeiou':
        cont += 1

print(f'Na string "{texto.capitalize()}" temos {cont} vogais presentes')

print('\nSao essas vogais:')
for vogais in texto:
    if vogais in 'aeiou':
        print(vogais, end=' ')