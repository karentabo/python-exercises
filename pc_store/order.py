class Order:
    count_id = 0

    def __init__(self):
        Order.count_id += 1
        self.id = Order.count_id
        self.computers = []

    def add_computer(self, computer):
        self.computers.append(computer)

    def __str__(self):
        computers_str = ''

        for computer in self.computers:
            computers_str += '\n' + str(computer)
        return f'Order #{self.id}{computers_str}'

    @classmethod
    def get_count_id(cls):
        return cls.count_id
