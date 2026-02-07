from movies_catalog.movie import Movie
from movies_catalog.movie_info import MovieInfo

movie_info = MovieInfo()
movie_info.load_movies()

def menu():
    print('-' * 20)
    print('*** Movie Catalog ***')

    while True:
        print('1. Add Movie')
        print('2. View all Movies')
        print('3. Remove a movie')
        print('4. Clear catalog list')
        print('5. Exit')

        option = input("Choose option: ")

        if not option.isdigit():
            print("Please enter only numbers.")
            continue

        option = int(option)

        if not (1 <= option <= 5):
            print('Enter a number between 1 and 5')
            continue

        return option


while True:
    option = menu()

    if option == 1:
        movie_name = input('Enter Movie Name: ')
        movie_info.add_movies(Movie(movie_name.title()))

    elif option == 2:
        movie_info.show_movies()

    elif option == 3:
        name = input('Movie name to remove: ')
        movie_info.remove_movie(name)

    elif option == 4:
        movie_info.clear_list()

    elif option == 5:
        print('Bye!')
        break
