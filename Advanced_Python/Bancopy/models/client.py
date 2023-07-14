from datetime import date

from utils.helper import date_to_str, str_to_date


class Client:

    count: int = 101

    def __init__(self: object, name: str, email: str, id: str, b_date: str) -> None:
        self.__code: int = Client.count
        self.__name: str = name
        self.__email: str = email
        self.__id: str = id
        self.__b_date: date = str_to_date(b_date)
        self.__date_reg: date = date.today()
        Client.count += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def id(self: object) -> str:
        return self.__id

    @property
    def b_date(self: object) -> str:
        return date_to_str(self.__b_date)

    @property
    def date_reg(self: object) -> str:
        return date_to_str(self.__date_reg)

    def __str__(self: object) -> str:
        return f'Code: {self.code} \nName: {self.name} \nBirth Date: {self.b_date} \n' \
               f'Registration Date: {self.date_reg}'



