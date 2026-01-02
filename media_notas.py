print('** MEDIA DE NOTAS **')

qtd_notas = int(input('Digite quantas notas serao adicionadas: '))

notas = []

for i in range (qtd_notas):
    nota = float(input(f'Digite a {i + 1}a nota: '))
    notas.append(nota)

print(f'As notas enviadas sao {notas}')

#soma dos valores na lista // media
soma_notas = sum(notas)
media = soma / qtd_notas

print(f'A media eh {media:.1f}')

