class InputDevice:

    def __init__(self, brand):
        self._brand = brand

    @property
    def brand(self):
        return self._brand