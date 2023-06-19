class Fighter():
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def __str__(self): return f"Fighter {self.name}, {self.health}, {self.damage_per_attack}"


def declare_winner(fighter1, fighter2, first_attacker):

    if fighter1.name == first_attacker:
        while fighter1.health > 0 and fighter2.health > 0:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
        pass
    elif fighter2.name == first_attacker:
        while fighter2.health > 0 and fighter1.health > 0:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name