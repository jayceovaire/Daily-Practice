from Item import Item

class Keyboard(Item):
    pay_rate = 0.7
    keyboards = []
    def __init__(self, name: str, price: float, quantity=0):
        #Call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)

        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero!"
        #Assign to self object
        self.name = name
        self.__price = price
        self.quantity = quantity

        #Actions to execute
        Keyboard.keyboards.append(self)
