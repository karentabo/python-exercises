print('** LISTA DE REPRODUCAO **')

num_musicas = int(input('Quantas musicas voce deseja adicionar em sua playlist? '))

playlist = []

#adicionando as musicas
for i in range(num_musicas):
    musica = input(f'Digite a {i + 1}a musica: ')
    playlist.append(musica)

#Organizar em ordem alfabetica
#playlist.sort(reverse=True)
playlist.sort()

#impressao da lista
print(f'As musicas da sua reproducao sao: ')
for musica in playlist:
    print(musica)