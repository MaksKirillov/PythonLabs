BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """
        Документация на класс Book.
        Класс описывает модель книги.
    """

    def __init__(self, id_: int, name: str, pages: int):
        """ Инициализация экземпляра класса.
            :param id_: Идентификатор книги;
            :param name: Название книги;
            :param pages: Количество страниц в книге.
        """
        self.id_ = None
        self.init_id(id_)

        self.name = None
        self.init_name(name)

        self.pages = None
        self.init_pages(pages)

    def __str__(self) -> str:
        """Определение метода __str__. """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Определение метода __repr__. """
        return f'Book(id_={self.id_}, name=\'{self.name}\', pages={self.pages})'

    def init_id(self, id_: int):
        """ Инициализация идентификатора книги. """
        if not isinstance(id_, int):
            raise TypeError("Wrong type of id, must be int")
        if id_ <= 0:
            raise ValueError("Id of book must be positive")
        self.id_ = id_

    def init_name(self, name: str):
        """ Инициализация названия книги. """
        if not isinstance(name, str):
            raise TypeError("Wrong type of name, must be str")
        self.name = name

    def init_pages(self, pages: int):
        """ Инициализация кол-ва страниц в книге. """
        if not isinstance(pages, int):
            raise TypeError("Wrong type of pages, must be int")
        if pages <= 0:
            raise ValueError("Number of pages must be positive")
        self.pages = pages


class Library:
    """
            Документация на класс Library.
            Класс описывает модель библиотеки.
    """

    def __init__(self, books=None):
        """ Инициализация экземпляра класса.
            :param books: Список книг.
        """

        self.books = books
        self.init_books(books)

    def init_books(self, books: list):
        """ Инициализация идентификатора книги. """
        if books is None:
            self.books = []
        else:
            if not isinstance(books, list):
                raise TypeError("Wrong type of books, must be list")
            for book in books:
                if not isinstance(book, Book):
                    raise TypeError("Wrong type of book, must be class Book")

    def get_next_book_id(self) -> int:
        """ Метод, возвращающий идентификатор для
        добавления новой книги в библиотеку.  """
        if not self.books:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int) -> int:
        """ Метод, возвращающий индекс книги в списке,
         который хранится в атрибуте экземпляра класса.  """
        for i, book in enumerate(self.books):
            if book.id_ == id_:
                return i


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
