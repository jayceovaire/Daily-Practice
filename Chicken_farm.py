import random
"""Chicken Farm Simulator"""

global feed
feed = 0


class Chicken:

    def __init__(self, name='Chicken'):
        self.name = name
        eggs = {'eggs': 0}
        self.eggs = eggs
        feathers = {'feathers': 0}
        self.feathers = feathers

    def __repr__(self):
        return self.name

    def lay_egg(self):
        print(f"{self.name} laid and egg!")
        self.eggs['eggs'] += 1

    def check_eggs(self):
        for chicken in farmer1.chickens:
            print(f"{chicken} {self.eggs}")

    def run(self):
        print(f"{self.name} runs around aimlessly!")

    def sit(self):
        print(f"{self.name} sits")

    def cluck(self):
        print(f'{self.name} says "Bawka Bawka Bawk"')

    def shuffle(self):
        print(f'{self.name} shuffles its feathers')
        chance = ['drop', 'nothing']
        feather_drop = random.choice(chance)
        if feather_drop == 'drop':
            self.feathers['feathers'] += 1
        if feather_drop == 'nothing':
            pass

    def peck(self, target=None):
        if target is None:
            print(f"{self.name} pecks at the ground")
            global feed
            if feed == 0:
                print('There is no feed left on the ground')
            if feed < 15:
                feed -= feed
            else:
                feed -= 15
        else:
            print(f"{self.name} pecks {target}")


class Farmer:

    def __init__(self, name='John'):
        self.name = name
        chickencount = 0
        chickens = []
        self.ccount = chickencount
        self.chickens = chickens

    def create_chicken(self, number=1):
        for i in range(number):
            self.ccount += 1
            chicken = Chicken(name=f"Chicken_{self.ccount}")
            self.chickens.append(chicken)

    def throw_feed(self):
        print(f"Farmer {self.name} throws more seed on the ground")
        global feed
        feed += 50

    def feed_chickens(self):
        print(f"Farmer {self.name} feeds the chickens")
        global feed
        feed += 50
        for chicken in farmer1.chickens:
            chicken.peck()
            print(f"{feed} feed remaining\n")

farmer1 = Farmer()
