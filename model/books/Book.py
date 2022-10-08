class Book:

    def __init__(self, book_id, title, type, auther, book_status):
        self.__book_id = book_id
        self.__title = title
        self.__type = type
        self.__auther = auther
        self.__book_status = book_status

    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_type(self):
        return self.__type

    def get_auther(self):
        return self.__auther

    def get_book_status(self):
        return self.__book_status

    def set_book_status(self, book_status):
        self.__book_status = book_status
