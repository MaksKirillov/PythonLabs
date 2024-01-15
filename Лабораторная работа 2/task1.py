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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
