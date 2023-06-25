
class Fighter():
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        self.original_health = health
    def __str__(self): return f"Fighter {self.name}, {self.health}, {self.damage_per_attack}"

class Cheater(Fighter):
    """Inherits the attributes of the Fighter class and has an extra attribute of its own"""
    def __init__(self, name, health, damage_per_attack, cheating_bonus=0):
        super().__init__(name, health, damage_per_attack)
        self.cheating_bonus = cheating_bonus
        self.damage_per_attack = cheating_bonus + damage_per_attack


def declare_winner(fighter1, fighter2, first_attacker):
    """
    fighter's health is restored to full before their fight.
    fighters take turns striking each other, the first strike is thrown by the first_attacker, once one
    of their health is reduced to 0 they lose and the winner is returned
    """
    fighter1.health = fighter1.original_health
    fighter2.health = fighter2.original_health

    if fighter1.name == first_attacker.name:
        while fighter1.health > 0 and fighter2.health > 0:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name

    elif fighter2.name == first_attacker.name:
        while fighter2.health > 0 and fighter1.health > 0:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <= 0:
                return fighter2.name
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <= 0:
                return fighter1.name


def main():
    HEALTH = 10 # Constant for fighter hp
    ATTACK = 2 # Constant for fighter atk
    frank_cheats = 1 # random variable
    player1 = Fighter('Joe', HEALTH, ATTACK)
    player2 = Fighter('Bob', HEALTH, ATTACK)
    player3 = Cheater('Frank', HEALTH, ATTACK, frank_cheats)
    # extra parameter is 0 by default but we pass it the frank_cheats variable
    # as you can see above, Frank is the Cheater class a sub-class of the Fighter class
    player4 = Fighter('Jim', HEALTH, ATTACK)

    print(player1)  # print __str__(self) = Fighter Joe, 10, 2
    print(player2)  # print __str__(self) = Fighter Bob, 10, 2
    print(player3)  # print __str__(self) = Fighter Frank, 10, 3
    print(player4)  # print __str__(self) = Fighter Jim, 10, 2

    first_fight = declare_winner(player2, player1, player2)
    first_fight_rematch = declare_winner(player2, player1, player1)
    print(first_fight, 'Wins!') #print Bob Wins!
    print(first_fight_rematch, 'Wins!') #print Joe Wins!
    second_fight = declare_winner(player4, player3, player4)
    print(second_fight, 'Wins!')  # print Frank Wins!
    third_fight = declare_winner(player3, player2, player2)
    print(third_fight, 'Wins the Tournament!') #print Frank wins the tournament!


main()
