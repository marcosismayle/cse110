with open('books_and_chapters.txt') as books_file:
    
    largest_chapter = -1
    largest_book = ''
    
    for book in books_file:
        
        clean_line = book.strip()
        parts = clean_line.split(':')

        book = parts[0]
        chapter = int(parts[1])
        scripture = parts[2]


        largest_chapter = max(chapter, largest_chapter)    
    
        if chapter == largest_chapter:
        
            largest_book =  book        


        print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter}')

    print(f'\nThe largest book is {largest_book.capitalize()} with {largest_chapter}.\n')