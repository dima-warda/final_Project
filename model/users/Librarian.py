from model.users.Person import Person


class Librarian(Person):

    def __init__(self, username, password, id_no, name, age, emp_type):
        super(Librarian, self).__init__(username=username, password=password, id_no=id_no, name=name, age=age)
        self.__emp_type = emp_type

    def get_emp_type(self):
        return self.__emp_type
