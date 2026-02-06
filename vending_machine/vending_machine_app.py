from vending_machine.snacks import Snack
from vending_machine.snacks_info import SnackInfo

snack_info = SnackInfo()
snack_info.load_snacks()

cart = []

def print_menu():
    print('\n*** Menu ***')
    print('1. Add Snack')
    print('2. Show Snacks')
    print('3. Buy Snack')
    print('4. Cart')
    print('5. Exit')

def handle_add_snack():
    name = input('Enter your Snack name: ').capitalize().strip()
    price_text = input('Enter your Snack price: ').strip()

    try:
        price = float(price_text)
    except ValueError:
        print('*** Invalid price ***')
        return

    snack = Snack(name, price)
    snack_info.add_snack(snack)

def handle_show_snacks():
    snack_info.show_snacks()

def handle_buy_snack():
    id_text = input('Enter your Snack ID: ').strip()
    if not id_text.isdigit():
        print('*** Invalid ID ***')
        return

    id_snack = int(id_text)
    snack_info.buy_snack(id_snack, cart)

def handle_cart():
    if not cart:
        print('*** Cart is empty ***')
        return

    summary = {}
    for item in cart:
        if item.id_snack not in summary:
            summary[item.id_snack] = {'snack': item, 'qty': 1}
        else:
            summary[item.id_snack]['qty'] += 1

    total = 0.0
    print('\n\t*** Cart ***')
    for data in summary.values():
        snack = data['snack']
        qty = data['qty']
        subtotal = snack.price * qty
        print(f'{snack.name} x{qty} -> $ {subtotal:.2f}')
        total += subtotal

    print('\t--- Total ---')
    print(f'\t\t $ {total:.2f}')

def handle_exit():
    yn = input('Are you sure you want to exit? y/n: ').lower().strip()
    return yn == 'y'

def menu():
    sair = False

    while not sair:
        print_menu()
        option = input('Enter your choice: ').strip()

        if not option.isdigit():
            print('*** Invalid option ***')
            continue

        option = int(option)

        if option == 1:
            handle_add_snack()
        elif option == 2:
            handle_show_snacks()
        elif option == 3:
            handle_buy_snack()
        elif option == 4:
            handle_cart()
        elif option == 5:
            sair = handle_exit()
        else:
            print('*** Invalid option ***')

print('\n*** Available Snacks ***')
snack_info.show_snacks()

menu()
