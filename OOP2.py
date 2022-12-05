from Item import Item
from Phone import Phone
from Keyboard import Keyboard

item1 = Keyboard("jscKeyboard", 1000, 3)
item2 = Phone("iphone14", 1200, 2)

item1.apply_discount()

print(Keyboard.keyboards)
print(Phone.phones)
print(Item.all)
