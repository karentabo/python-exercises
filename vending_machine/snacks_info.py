from vending_machine.snacks import Snack

class SnackInfo:
    FILE_NAME = 'add_snacks.txt'

    def __init__(self):
        self.snacks = []

    def add_snack(self, snack: Snack):
        self.snacks.append(snack)

        with open(self.FILE_NAME, 'a') as file:
            file.write(f'{snack.id_snack},{snack.name},{snack.price}\n')

        print("Snack added")
        print(f'ID: {snack.id_snack} | {snack.name} | $ {snack.price:.2f}')

    def load_snacks(self):
        self.snacks.clear()
        try:
            with open(self.FILE_NAME, 'r') as file:
                for line in file:
                    id_snack, name, price = line.strip().split(',')

                    snack = Snack(name, float(price))
                    snack.id_snack = int(id_snack)

                    self.snacks.append(snack)
                    Snack.count_snacks = snack.id_snack
        except FileNotFoundError:
            pass

    def show_snacks(self):
        self.load_snacks()

        if not self.snacks:
            print("*** No snacks saved yet ***")
        else:
            for snack in self.snacks:
                print(snack)

    def buy_snack(self, id_snack: int, cart: list):
        self.load_snacks()

        for snack in self.snacks:
            if snack.id_snack == id_snack:
                cart.append(snack)
                print(f'Added to cart: {snack}')
                return

        print('*** Snack not found ***')
