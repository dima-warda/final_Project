from model.users.Person import Person


class Client(Person):

    def __init__(self, username, password, id_no, name, age, phone_number):
        super().__init__(username=username, password=password, id_no=id_no, name=name, age=age)
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number
