MEMORY_IN_MB = 1.44
PAGES_IN_BOOK = 100
LINES_IN_PAGE = 50
SYMBOLS_IN_LINE = 25
BYTES_IN_SYMBOL = 4

memory_in_bytes = int(round(MEMORY_IN_MB * 1024 * 1024, 0))
bytes_in_book = PAGES_IN_BOOK * LINES_IN_PAGE * SYMBOLS_IN_LINE * BYTES_IN_SYMBOL
books_in_memory = memory_in_bytes // bytes_in_book

print("Количество книг, помещающихся на дискету:", books_in_memory)
