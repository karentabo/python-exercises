from pc_store.monitor import Monitor
from pc_store.keyboard import Keyboard
from pc_store.mouse import Mouse
from pc_store.computer import Computer
from pc_store.order import Order

monitor1 = Monitor("Dell", "27")
keyboard1 = Keyboard("Logitech")
mouse1 = Mouse("Razer")
computer1 = Computer("Gaming PC", monitor1, keyboard1, mouse1)

monitor2 = Monitor("Samsung", "32")
keyboard2 = Keyboard("Corsair")
mouse2 = Mouse("Corsair")
computer2 = Computer("Gaming PC", monitor2, keyboard2, mouse2)

order1 = Order()
order1.add_computer(computer1)
order2 = Order()
order2.add_computer(computer2)

print(order1)
print(order2)