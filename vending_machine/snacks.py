class Snack:
    count_snacks = 0

    def __init__(self, name, price):
        Snack.count_snacks += 1
        self.id_snack = Snack.count_snacks
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f'ID: {self.id_snack} | {self.name} | $ {self.price:.2f}'