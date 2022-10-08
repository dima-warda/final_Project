class Utils:
    ACTIVE = 1
    INACTIVE = 2
    EXPIRED = 3
    CANCELED = 4
    FULL_TIME = "A"
    PART_TIME = "B"


class Cons_methods:

    @staticmethod
    def is_value_empty(*value: str):
        for item in value:
            if  item == "":
                return True

