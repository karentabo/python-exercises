class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self._title = title
        self._author = author
        self._genre = genre

    @property
    def id(self):
        return self.book_id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def genre(self):
        return self._genre

#only read code
    # @title.setter
    # def title(self, new_title):
    #     self._title = new_title
    #
    # @author.setter
    # def author(self, new_author):
    #     self._author = new_author
    #
    # @genre.setter
    # def genre(self, new_genre):
    #     self._genre = new_genre
