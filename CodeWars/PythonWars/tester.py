class Player():
    def __init__(self, name, age, CONSTANT):
        self.name = name
        self.age = age
        self.startpoint = 1

        if name == 'player2':
            self.startpoint = 2 # you can change the attribute of a class with logic

        if CONSTANT != 1:
            print('constant does not equal 1')
        else:
            print('constant equals 1')

    def printname(self):
        print(self.name)

    def sayage(self):
        print(self.age)

    def changeage(self):
        self.age = input('what is your new age?') # will change the age of the player


    def printvar(self, argument):
        print(argument)


# remove the duplicate class
# ________________________________________________________
class Other_player():
    def __init__(self, name, age, CONSTANT):
        self.name = name
        self.age = age
        self.startpoint = 2


    def printname(self):
        print(self.name)

    def sayage(self):
        print(self.age)

    def printvar(self, argument):
        print(argument)

    def randomfunction(self, CONSTANT):
        if CONSTANT != 1:
            print('constant does not equal 1')
# _________________________________________________________

def main():
    OTHER = 1
    CONSTANT = 500
    variable = 1
    player1 = Player('player1', 21, CONSTANT) # initialize a Player() class called player 1
    player2 = Player('player2', 18, OTHER) # initialize a Player() class called player 2

    game_active = True
    while game_active:
        player1.printname() #pints player 1 name
        player1.printvar(variable)#prints variable = 1
        player2.printname()# prints player 2 name
        player1.sayage()# prints self.age in this case it is 21
        player1.changeage() #prompts user to change their age
        player1.sayage()# prints new self.age
        # adding an escape from the loop so I can stop the program
        game_active = False

main()