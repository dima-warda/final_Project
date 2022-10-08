from main_cotroller.user_login_cont import User
from model.users.Client import Client
from model.users.Person import Person
from model.users.Librarian import Librarian
from model.books.Book import Book
from model.books.Borrowing_order import Borrowing_Order
from utils.Utils import *


def new_iformation(new: User):
    name = input("Name : ")
    age = input("Age : ")
    phone_number = input("Phone Number : ")
    if Cons_methods.is_value_empty(name, age, phone_number):
        print("Please, Enter All Your Information ")
        return
    new_clint = Client(name=name, age=age, phone_number=phone_number, username=username, password=password,
                       id_no=User.get_cl_last_id(user) + 1)
    new.creat_client_account(new_clint)


def new_book(em_b: User):
    print("\nInter The Book Information : \n")

    book_name = input("Book Name : ")
    b_type = input("Type : ")
    b_auther = input("Auther Of Book : ")
    b_status = input("book_status : ")
    n_book = Book(title=book_name, type=b_type, auther=b_auther, book_status=b_status,
                  book_id=User.get_bo_last_id(user) + 1)
    em_b.creat_new_book(n_book)

    if Cons_methods.is_value_empty(book_name, b_type, b_auther, b_status):
        print("Please, Enter All The Book Information ")
    else:
        print("The Book has been added")


def new_ordr(ne_ord: User):
    print("\nInter The Order Information : \n")

    book_id = input("Book Id : ")
    borro_dat = input("Date : ")
    cl_id = input("Your Id : ")
    n_order = Borrowing_Order(id=User.get_bor_last_id(user) + 1, date=borro_dat, order_status=Utils.ACTIVE,
                              client_id=cl_id, book_id=book_id)
    ne_ord.creat_new_order(n_order)
    # if user.check_book_existence_id == book_id :
    #     Book.set_book_status(book_status=Utils.INACTIVE)
    if not user.check_book_existence_id or book_id != user.check_book_existence_id:
        print("This Book Id Is Not Existed !")
    elif not user.check_clint_existence_id or cl_id != user.check_clint_existence_id:
        print("Your Id Is Not Existed!")
    elif Cons_methods.is_value_empty(book_id, borro_dat, cl_id):
        print("Please, Enter All The Order Information ")
    else:
        print("The Order has been added")


def return_ordr(ne_ord: User):
    print("\nInter The Order Information : \n")

    book_id = input("Book Id : ")
    borro_dat = input("Dat : ")
    cl_id = input("Your Id : ")
    n_order = Borrowing_Order(id=User.get_bor_last_id(user) + 1, date=borro_dat, order_status=Utils.EXPIRED,
                              client_id=cl_id, book_id=book_id)
    ne_ord.creat_new_order(n_order)
    # if user.check_book_existence_id == book_id :
    #     Book.set_book_status(book_status=Utils.ACTIVE)
    if not user.check_book_existence_id or book_id != user.check_book_existence_id:
        print("This Book Id Is Not Existed !")
    elif not user.check_clint_existence_id or cl_id != user.check_clint_existence_id:
        print("Your Id Is Not Existed!")

    elif Cons_methods.is_value_empty(book_id, borro_dat, cl_id):
        print("Please, Enter All The Order Information ")
    else:
        print("The Book has been returned")


def search_for_order(id: int, borrowing_order: list[Borrowing_Order]):
    if Borrowing_Order == None or len(borrowing_order) == 0:
        return True
    else:
        for item in borrowing_order:
            if item.get_id() == id:
                return item


def search_for_client(id: int, client: list[Client]):
    if Client == None or len(client) == 0:
        return True
    else:
        for item in client:
            if item.get_id_no() == id:
                return item


def search_for_book(id: int, book: list[Book]):
    if Book == None or len(book) == 0:
        return True
    else:
        for item in book:
            if item.get_book_id() == id:
                return item


print("User_Type : 1_Clint   2_Librarian ")
user_type = input("Choose Your User_Type : ")
if user_type == 1:
    pass
if user_type == 2:
    pass
user = User()
username = input("Username : ")
password = input("Password : ")
if Cons_methods.is_value_empty(username, password):
    print("Error, Make sure if you entered all the inputs")
    exit()

user = User()

if user.librarian_login(username, password):
    print("User Permission : 1_Search for client accounts    2_ Book Information    3_Add New Book    4_Order")
    want = input("\nWhat Do You Want : ")
    if want == "1":
        for item in User.client:
            cli_id = input("\nInter Client Id :  \n")
            if not Cons_methods.is_value_empty(cli_id) and cli_id.isdigit():
                find_client = search_for_client(int(cli_id), user.get_clint())

                if find_client != True:
                    print("Client Name : ", find_client.get_name()
                          , "\nStudent Age : ", find_client.get_age(),
                          "\nPhone Number : ", find_client.get_phone_number())

    elif want == "2":
        for item in User.book:
            book_id = input("\nInter Book Id :  ")
            if not Cons_methods.is_value_empty(book_id) and book_id.isdigit():
                find_book = search_for_book(int(book_id), user.get_book())

                if find_book != True:
                    print("Book Title : ", find_book.get_title()
                          , "\nBook Type : ", find_book.get_type(),
                          "\nBook Auther : ", find_book.get_auther(),
                          "\nBook Status : ", find_book.get_book_status())

    elif want == "3":
        new_book(user)

    elif want == "4":
        print(User.borrowing_order)

elif user.client_login(username, password):
    print("User Permission : 1_Make New Order    2_Return Book   3_My Order")
    want2 = input("What Do You Want : ")

    if want2 == "1":
        print(User.active_books)
        new_ordr(user)

    elif want2 == "2":
        return_ordr(user)


    elif want2 == "3":
        for item in user.borrowing_order:
            your_id = input("\nYour Id : ")
            if not Cons_methods.is_value_empty(your_id) and your_id.isdigit():
                find_order = search_for_order(int(your_id), user.get_borroing_order())

                if find_order != True:
                    print("Borrowing Date : ", find_order.get_date()
                          , "\nOrder Status : ", find_order.get_order_status(),
                          "\nBook Id : ", find_order.get_book_id())
            break

elif not user.check_user_existence(username):
    print("Creat New Account : \n")
    new_iformation(user)
