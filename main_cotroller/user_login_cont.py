from model.users.Client import Client
from model.users.Librarian import Librarian
from model.books.Book import Book
from model.books.Borrowing_order import Borrowing_Order
from utils.Utils import Utils


class User:
    client: list[Client] = [Client("محمد_19", "1842", 1, " محمد عبد الكريم", 19, "1655816"),
                            Client("@majd", "4761", 2, " مجد سالم  ", 14, "1476329"),
                            Client("mariam_sr", "5792", 3, " مريم خالد", 27, "5419763")]

    librarian: list[Librarian] = [Librarian("سمير", "7469", 1, " سمير مجدي", 42, "7452019"),
                                  Librarian("نور", "9720", 2, " نور الهدى ", 36, "8456103"),
                                  Librarian("ملك47", "6410", 3, " ملك هلال ", 27, "4125973")]

    book: list[Book] = [Book(1, "The Prince", "سياسي", "Niccolò Machiavelli", Utils.ACTIVE),
                        Book(2, "مع الله", "علوم اسلامية", "سلمان العودة", Utils.INACTIVE),
                        Book(3, "the stranger", "رواية", "Albert Camus", Utils.ACTIVE),
                        Book(4, "الثلاثية", "رواية", "نجيب محفوظ", Utils.ACTIVE),
                        Book(5, "أربعون", "سيرة ذاتية", "أحمد الشقيري", Utils.INACTIVE)]

    active_books: list[Book] = [Book(1, "The Prince", "سياسي", "Niccolò Machiavelli", Utils.ACTIVE),
                                Book(3, "the stranger", "رواية", "Albert Camus", Utils.ACTIVE),
                                Book(4, "الثلاثية", "رواية", "نجيب محفوظ", Utils.ACTIVE)]

    borrowing_order: list[Borrowing_Order] = [Borrowing_Order(1, "4/NOV", Utils.CANCELED, 3, 2),
                                              Borrowing_Order(2, "2/OCT", Utils.ACTIVE, 2, 1),
                                              Borrowing_Order(3, "30/SEP", Utils.ACTIVE, 1, 5),
                                              Borrowing_Order(4, "27/SEP", Utils.EXPIRED, 2, 3)]

    def get_clint(self):
        return self.client

    def get_book(self):
        return self.book

    def get_active_books(self):
        return self.active_books

    def get_borroing_order(self):
        return self.borrowing_order

    def librarian_login(self, username: str, password: str) -> bool:
        for item in self.librarian:
            if username == item.get_username() and password == item.get_password():
                return True

    def client_login(self, username: str, password: str) -> bool:
        for item in self.client:
            if username == item.get_username() and password == item.get_password():
                return True

    def check_user_existence(self, username: str):
        for item in self.client:
            if username == item.get_username():
                return True

    def creat_client_account(self, user: Client):
        for item in self.client:
            if not self.check_user_existence(user.get_username()):
                return self.client.append(user)

    def check_book_existence(self, title: str):
        for item in self.book:
            if title == item.get_title():
                return True

    def check_book_existence_id(self, book_id: int):
        for item in self.book:
            if book_id == item.get_book_id():
                return True

    def check_clint_existence_id(self, id_no: int):
        for item in self.client:
            if id_no == item.get_id_no():
                return True

    def creat_new_book(self, nw_book: Book):
        for item in self.book:
            if not self.check_book_existence(nw_book.get_title()):
                return self.book.append(nw_book)

    def check_book_status(self, check_book: Book):
        for item in self.book:
            if Book.get_book_status(check_book) == Utils.ACTIVE:
                return self.active_books.append(check_book)

    def check_order_existence(self, id: int):
        for item in self.borrowing_order:
            if id == item.get_id():
                return True

    def creat_new_order(self, nw_order: Borrowing_Order):
        for item in self.borrowing_order:
            if not self.check_order_existence(nw_order.get_id()):
                return self.borrowing_order.append(nw_order)

    def get_cl_last_id(self) -> int:
        return self.client[len(self.client) - 1].get_id_no()

    def get_bo_last_id(self) -> int:
        return self.book[len(self.book) - 1].get_book_id()

    def get_bor_last_id(self) -> int:
        return self.borrowing_order[len(self.client) - 1].get_id()
