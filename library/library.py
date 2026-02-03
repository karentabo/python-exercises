from books import Book

class Library:
    _count_id = 1

    def __init__(self, name):
        self._name = name
        self._books = []

    def add_book(self, title, author, genre):
        book = Book(Library._count_id, title, author, genre)
        Library._count_id += 1
        self._books.append(book)
        return book

    def total_books(self):
        return len(self._books)

    def search_by_title(self, title):
        title = title.lower().strip()
        for book in self._books:
            if book.title.lower().strip() == title:
                return book
        return None

    def search_by_author(self, author):
        author = author.lower().strip()
        result = []

        for book in self._books:
            if book.author.lower().strip() == author:
                result.append(book)

        return result

    def search_by_genre(self, genre):
        genre = genre.lower().strip()
        result = []

        for book in self._books:
            if book.genre.lower().strip() == genre:
                result.append(book)

        return result

    def show_all_books(self):
        return self._books

    @property
    def name(self):
            return self._name

    @property
    def books(self):
            return self._books