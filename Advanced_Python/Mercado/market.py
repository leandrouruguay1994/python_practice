from typing import List, Dict, Union
from time import sleep

from models.product import Product
from utils.helper import format_float_str_currency

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    print('=======================')
    print('======= Welcome! ======')
    print('=======   Shop   ======')
    print('=======================')

    print('Select your option below: ')
    print('1 - Add product')
    print('2 - List products')
    print('3 - Buy products')
    print('4 - Check cart')
    print('5 - Close cart')
    print('6 - Exit')

    option: int = int(input())

    if option == 1:
        add_product()
    elif option == 2:
        list_products()
    elif option == 3:
        buy_product()
    elif option == 4:
        check_cart()
    elif option == 5:
        close_cart()
    elif option == 6:
        print('Thanks for your time!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option!')
        sleep(1)
        menu()

def add_product() -> None:
    print('Adding product')
    print('==============')

    name: str = input('Product name: ')
    price: float = float(input('Product price: '))

    product: Product = Product(name, price)

    products.append(product)

    print(f'The product {product.name} has been added successfully!')
    sleep(2)
    menu()

def list_products() -> None:
    if len(products) > 0:
        print('listing products')
        print('================')

        for product in products:
            print(product)
            print()
            print('------------------')
            sleep(1)
    else:
        print('There are no products added yet!')
    sleep(2)
    menu()

def buy_product() -> None:
    if len(products) > 0:
        print("Please, type the prouct's code and add it to the cart: ")
        print('--------------------------------------------------------')
        print('===================== Available Products ===============')
        for product in products:
            print(product)
            print('-------------------')
            sleep(1)
        code: int = int(input())

        product: Product = look_product_from_code(code)

        if product:
            if len(cart) > 0:
                it_is_added: bool = False
                for item in cart:
                    quant: int = item.get(product)
                    if quant:
                        item[product] += 1
                        print(f'The product {product.name} now has {quant + 1} uds in the cart.')
                        it_is_added = True
                        sleep(2)
                        menu()
                if not it_is_added:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'The product {product.name} has been added to the cart.')
                    sleep(2)
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f'The product {product.name} has been added to the cart!')
                sleep(2)
                menu()
        else:
            print(f'The product with code {code} was not founded.')
            sleep(2)
            menu()
    else:
        print('There are no products yet')
    sleep(2)
    menu()

def check_cart() -> None:
    if len(cart) > 0:
        print('Products in the cart: ')

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Quantity: {data[1]}')
                print('--------------------')
                sleep(1)
    else:
        print('There are no products in the cart.')
        sleep(2)
        menu()

def close_cart() -> None:
    if len(cart) > 0:
        total_val: float = 0

        print('Products inside the cart')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Qunantity: {data[1]}')
                total_val += data[0].price * data[1]
                print('-------------------------------')
                sleep(1)
        print(f'Your invoice is: {format_float_str_currency(total_val)}')
        print('See you later!')
        cart.clear()
        sleep(5)
    else:
        print('The cart is empty')
    sleep(2)
    menu()

def look_product_from_code(code: int) -> Union[Product, None]:
    p: Product = None

    for product in products:
        if product.code == code:
            p = product
    return p

if __name__ == '__main__':
    main()

