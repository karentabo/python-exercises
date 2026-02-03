from library import Library

national_library = Library('National Library')

print(f'*** Welcome to the {national_library.name} ***')

def menu():
    print('\nMenu: ')
    print('1. Add a book')
    print('2. View all books')
    print('3. Search a book by title')
    print('4. Search a book by author')
    print('5. Search a book by genre')
    print('6. Exit')

    while True:
        option = input('Select an option: ').strip()

        if not option.isdigit():
            print('Please enter a number.')
            continue

        option = int(option)
        if 1 <= option <= 6:
            return option
        else:
            print('Select a number between 1 and 6.')

running = True

while running:
    option = menu()

    if option == 6:
        while True:
            print('Are you sure you want to exit? (y/n)')
            y_n = input('Enter y/n: ').lower().strip()
            if y_n == 'y':
                print('Exiting....')
                running = False
                break
            elif y_n == 'n':
                break
            else:
                print('Invalid option')

    elif option == 1:
        title = input('Enter a book title: ')
        author = input('Enter a book author: ')
        genre = input('Enter a book genre: ')

        national_library.add_book(title, author, genre)

        print(f'Title: {title}, Author: {author}, Genre: {genre}')
        print(f'Book added successfully!')

    elif option == 2:
        books = national_library.show_all_books()

        if not books:
            print('No books found.')
        else:
            for book in books:
                print(f"ID: {book.id} | {book.title} | {book.author} | {book.genre}")

    elif option == 3:
        title = input('Enter the book title: ')
        book = national_library.search_by_title(title)

        if book is None:
            print('Book not found.')
        else:
            print(f'Title: {book.title}')
            print(f'Author: {book.author}')
            print(f'Genre: {book.genre}')

    elif option == 4:
        author = input('Enter the book author: ')
        books = national_library.search_by_author(author)

        if books is None:
                print('Book not found.')
        else:
            print(f'Books found from author: {author}')
            for book in books:
                print(f'Title: {book.title}')
                print(f'Author: {book.author}')
                print(f'Genre: {book.genre}')
                print('-' * 15)

    elif option == 5:
        genre = input('Enter the book genre: ')
        books = national_library.search_by_genre(genre)

        if books is None:
                print('Book not found.')
        else:
            print(f'Book(s) found from genre: {genre}')
            for book in books:
                print(f'Title: {book.title}')
                print(f'Author: {book.author}')
                print(f'Genre: {book.genre}')
                print('-' * 15)





