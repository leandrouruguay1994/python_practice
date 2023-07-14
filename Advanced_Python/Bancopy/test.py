from models.client import Client
from models.account import Account

rupert: Client = Client('Rupert Diaz', 'rp@gmail.com', '12345678-9', '04/02/1982')
angelina: Client = Client('Angelina Jolie', 'ag@gmail.com', '84893829-3', '03/01/1945')

"""print(rupert)
print(angelina)"""

accountr: Account = Account(rupert)
accounta: Account = Account(angelina)

"""print(accountr)
print(accounta)"""



