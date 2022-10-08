class Person:
    age = 0
    id_no = 0

    def __init__(self, id_no, name, age, username, password):
        self.__username = username
        self.__password = password
        self.__id_no = id_no
        self.__name = name
        self.__age = age

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_id_no(self):
        return self.__id_no

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
