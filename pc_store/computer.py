from pc_store.keyboard import Keyboard
from pc_store.monitor import Monitor
from pc_store.mouse import Mouse


class Computer:
    count_id = 0

    def __init__(self,name: str, monitor: Monitor, keyboard: Keyboard, mouse: Mouse):
        Computer.count_id += 1
        self.id = Computer.count_id

        self.name = name
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse

    def __str__(self):
        return (f'Computer #{self.id}: {self.name}\n'
                f'{self.monitor}'
                f'{self.keyboard}'
                f'{self.mouse}')



    @classmethod
    def get_count_id(cls):
        return cls.count_id