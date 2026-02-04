class Monitor:
    count_id = 0

    def __init__(self, brand, size):
        Monitor.count_id += 1
        self.id = Monitor.count_id
        self.brand = brand
        self.size = size

    def __str__(self):
        return f'Monitor #{self.id}: {self.brand} - {self.size}"\n'

    @classmethod
    def get_count_id(cls):
        return cls.count_id