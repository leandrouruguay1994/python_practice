from typing import List
from time import sleep

from models.client import Client
from models.account import Account

accounts: List[Account] = []


def main() -> None:
    menu()


def menu() -> None:
    print('================================')
    print('============= ATM ==============')
    print('=========== MY BANK ============')
    print('================================')

    print('Select your option: ')
    print('1 - Create account')
    print('2 - Withdraw')
    print('3 - Deposit')
    print('4 - Transfer')
    print('5 - List Accounts')
    print('6 - Exit')

    option: int = int(input())

    if option == 1:
        create_acc()
    elif option == 2:
        withdraw_money()
    elif option == 3:
        make_deposit()
    elif option == 4:
        make_transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('Thank you for choosing us!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option')
        sleep(2)
        menu()


def create_acc() -> None:
    print("Please, report client's data")

    name: str = input("Client's name: ")
    email: str = input("E-mail: ")
    id: str = input("Client's id: ")
    b_day: str = input("Client's brithday: ")

    client: Client = Client(name, email, id, b_day)

    account: Account = Account(client)

    accounts.append(account)

    print('New account created successfully!')
    print('Account data: ')
    print('----------------------------------')
    print(account)
    sleep(2)
    menu()


def withdraw_money() -> None:
    if len(accounts) > 0:
        number: int = int(input('Please, report your account number: '))

        account: Account = look_account_code(number)

        if account:
            value: float = float(input('Please, inform how much you want to withdraw: '))

            account.withdraw(value)
        else:
            print(f'There is no account number {number}')
    else:
        print('No account has been created')
    sleep(2)
    menu()


def make_deposit() -> None:
    if len(accounts) > 0:
        number: int = int(input('Please, report your account number: '))

        account: Account = look_account_code(number)

        if account:
            value: float = float(input('Please, inform how much you want to deposit: '))

            account.deposit(value)
        else:
            print(f'There is no account number {number}')
    else:
        print('No account has been created')
    sleep(2)
    menu()


def make_transfer() -> None:
    if len(accounts) > 0:
        o_number: int = int(input('Please, report your account number: '))

        o_account: Account = look_account_code(o_number)

        if o_account:
            d_number: int = int(input('Please, report the destination account: '))

            d_account: Account = look_account_code(d_number)

            if d_account:
                value: float = float(input('Please, inform how much you want to transfer: '))

                o_account.transfer(d_account, value)
            else:
                print(f'There is no account number {d_number}')
        else:
            print(f'There is no account number {o_number}')
    else:
        print('No account has been created')
    sleep(2)
    menu()


def list_accounts() -> None:
    if len(accounts) > 0:
        print('Account list')

        for account in accounts:
            print(account)
            print('----------------------')
            sleep(1)
    else:
        print('No account has been created')
    sleep(2)
    menu()


def look_account_code(code: int) -> Account:
    a: Account = None

    if len(accounts) > 0:
        for account in accounts:
            if account.num == code:
                a = account
    return a

if __name__ == '__main__':
    main()