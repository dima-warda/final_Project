class Borrowing_Order:

    def __init__(self, id, date, order_status, client_id, book_id):
        self.__order_status = order_status
        self.__date = date
        self.__id = id
        self.__client_id = client_id
        self.__book_id = book_id

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_order_status(self):
        return self.__order_status

    def get_client_id(self):
        return self.__client_id

    def get_book_id(self):
        return self.__book_id
