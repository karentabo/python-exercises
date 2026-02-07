import os

from movies_catalog.movie import Movie

FILE_NAME = 'movies.txt'

class MovieInfo:
    def __init__(self):
        self.movies = []

    def __str__(self):
        return str(self.movies)

    def load_movies(self):
        self.movies.clear()

        seen = set()

        try:
            with open(FILE_NAME, 'r') as file:
                for line in file:
                    name = line.strip()

                    if name.lower() not in seen:
                        seen.add(name.lower())
                        self.movies.append(Movie(name))

        except FileNotFoundError:
            pass

    def add_movies(self, movie: Movie):

        new_name = movie.name.strip().title()

        if not new_name:
            print("Movie name can't be empty")
            return

        if any(m.name.lower() == new_name.lower() for m in self.movies):
            print(f'Movie "{new_name}" already exists in your catalog.')
            return

        self.movies.append(Movie(new_name))

        with open(FILE_NAME, 'a') as file:
            file.write(new_name + '\n')

        print(f'Movie "{new_name.title()}" added successfully!')

    def show_movies(self):
        if not self.movies:
            print('There is no catalog to show.')
            return
        print('*** Movies list ***')
        print('-' * 20)
        for movie in self.movies:
            print(f'- {movie}')

    def remove_movie(self, name: str):
        name = name.strip()
        target = name.lower()

        self.movies = [m for m in self.movies if m.name.strip().lower() != target]

        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            for m in self.movies:
                file.write(m.name.strip() + '\n')

        print(f'Movie "{name.title()}" removed successfully!')

    def clear_list(self):
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)
            self.movies.clear()
            print('Catalog removed successfully.')
        else:
            print('There is no catalog to remove.')
