with open('books.txt') as books_file:
    for line in books_file:
        book = line.strip()
        print(book)