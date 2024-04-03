class Item():
    def __init__(self, name, attack_bonus, health_bonus):
        self.name = name
        self.attack_bonus = attack_bonus
        self.health_bonus = health_bonus

    def __repr__(self):
        return self.name

class Sword(Item):
    def __init__(self, name, attack_bonus, health_bonus):
        super().__init__(name, attack_bonus, health_bonus)

poker = Item('poker', 1, 0)

steel_sword = Sword('Steel Sword', 5, 0)

class Player():
    def __init__(self, name, race, health, attack):
        self.name = name
        self.race = race
        self.health = health
        self.attack = attack
        self.equipped_item = None
        self.bag = {poker: 1}

    def __repr__(self):
        return self.name

    def basic_attack(self):
        total_attack = self.attack
        print(f'{self.name} swings for {total_attack} points')

    def equip_item(self, item):
        if item in self.bag:
            if isinstance(item, Item):
                self.equipped_item = self.bag[item]
                self.bag[item] -= self.equipped_item
                self.health += item.health_bonus
                self.attack += item.attack_bonus
                print(f'{self.name} equipped {item.name}. Health +{item.health_bonus}, Attack +{item.attack_bonus}')
        else:
            print('item is not in your bag')
    def unequip_item(self, item):
        if self.equipped_item:
            self.attack -= item.attack_bonus
            self.health -= item.health_bonus
            self.bag[item] += self.equipped_item
            self.equipped_item = None
        else:
            print('you dont have an item to unequip')

class Warrior(Player):
    def __init__(self, name, race, health, attack):
        super().__init__(name, race, health, attack)
        self.health = health
        self.attack += 2

    def war_shout(self):
        self.health += 5
        self.attack += 2

class Berserker(Warrior):
    def __init__(self, name, race, health, attack):
        super().__init__(name, race, health, attack)
        self.health -= 5
        self.attack += 10





player1 = Player('Winky', 'Dwarf', 10, 11)









