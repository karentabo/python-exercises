from pc_store.input_device import InputDevice

class Mouse(InputDevice):
    count_id = 0

    def __init__(self, brand):
        Mouse.count_id += 1
        self.id = Mouse.count_id

        super().__init__(brand)

    def __str__(self):
        return f'Mouse: #{self.id} - {self.brand}\n'

    @classmethod
    def get_count_id(cls):
        return cls.count_id