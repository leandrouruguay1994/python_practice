from models.client import Client
from utils.helper import format_float_str_curr

class Account:

    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__num: int = Account.code
        self.__client: Client = client
        self.__balance: float = 0
        self.__limit: float = 1000.00
        self.__tot_balance: float = self._cal_tot_balance
        Account.code += 1

    @property
    def num(self: object) -> int:
        return self.__num

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def balance(self: object) -> float:
        return self.__balance

    @balance.setter
    def balance(self: object, value: float) -> None:
        self.__balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def tot_balance(self: object) -> float:
        return self.__tot_balance

    @tot_balance.setter
    def tot_balance(self: object, value: float) -> None:
        self.__tot_balance = value

    @property
    def _cal_tot_balance(self: object) -> float:
        return self.balance + self.limit

    def __str__(self: object) -> str:
        return f'Account number: {self.num} \nClient: {self.client.name} \n' \
               f'Total Balance: {format_float_str_curr(self.tot_balance)}'

    def deposit(self: object, value: float) -> None:
        if value > 0:
            self.balance = self.balance + value
            self.tot_balance = self._cal_tot_balance
            print('Deposit made successfully!')
        else:
            print('Error. Try again.')

    def withdraw(self: object, value: float) -> None:
        if value > 0 and self.tot_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.tot_balance = self._cal_tot_balance
            else:
                leftover: float = self.balance - value
                self.limit = self.limit + leftover
                self.balance = 0
                self.tot_balance = self._cal_tot_balance
            print('Withdraw made successfully!')
        else:
            print('Error. Try again.')

    def transfer(self: object, d_account: object, value: float) -> None:
        if value > 0 and self.tot_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.tot_balance = self._cal_tot_balance
                d_account.balance = d_account.balance + value
                d_account.tot_balance = d_account._cal_tot_balance
            else:
                leftover: float = self.balance - value
                self.balance = 0
                self.limit = self.limit + leftover
                self.tot_balance = self._cal_tot_balance
                d_account.balance = d_account.balance + value
                d_account.tot_balance = d_account._cal_tot_balance
            print('Transfer successful.')
        else:
            print('Error. Try again.')

