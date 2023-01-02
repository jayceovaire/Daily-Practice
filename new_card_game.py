import random

# Define the deck and removed_cards lists outside of the Player class
deck = ['2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts',
        '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts',
        'King of Hearts', 'Ace of Hearts', '2 of Spades', '3 of Spades', '4 of Spades',
        '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades',
        'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', '2 of Clubs',
        '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs',
        '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs',
        '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds',
        '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds',
        'King of Diamonds', 'Ace of Diamonds', 'Joker', 'Joker']
removed_cards = []


class Board:
    def __init__(self):
        self.cards_in_play = []

    def add_card(self, card):
        self.cards_in_play.append(card)

    def remove_card(self, card):
        self.cards_in_play.remove(card)

    def clear_board(self):
        for card in self.cards_in_play:
            # iterate through cards in play and remove them
            self.cards_in_play.remove(card)
            # add cards in play to removed card list
            removed_cards.append(card)

    def view_cards(self):
        print("Cards in play:")
        for card in self.cards_in_play:
            print(card)


board = Board()


class Player:
    def __init__(self, name, deck, removed_cards, balance=1):
        self.name = name
        # Accept the deck and removed_cards lists as arguments and store them as instance variables
        self.deck = deck
        self.removed_cards = removed_cards  # cards that have been removed from the board or discarded
        self.hand = []  # cards in players hand
        self.board = board  # board class, used to pass arguments to the Board
        self.tokens = 0  # tokens player has
        self.rolled_dice = []  # list of most recently rolled dice
        self.current_bet = 0  # current bet player has waged
        self.balance = balance  # current balance player has available to bet on

    # place a bet
    def place_bet(self, bet_amount):
        self.current_bet += bet_amount
        self.balance -= bet_amount

    # raise current bet
    def raise_bet(self, raise_amount):
        self.current_bet += raise_amount
        self.balance -= raise_amount

    # fold, give up, lose current round
    def fold_bet(self):
        self.current_bet = 0

    # look at your current balance
    def view_balance(self):
        print(f"{self.name}'s balance is {self.balance}")

    # take winnings from bet
    def payout_winnings(self, winnings):
        self.balance += winnings

    # add tokens to player token count
    def add_tokens(self):
        self.tokens += 1

    # check number of tokens player has
    def view_tokens(self):
        print(f"{self.name} has {self.tokens} tokens\n")

    def view_hand(self):
        # Print the cards in the player's hand along with a number for each card
        print(f"{self.name}'s hand:")
        for i, card in enumerate(self.hand):
            print(f"{i + 1}. {card}")

    def swap_cards_with_player(self, other_player):
        # List of cards to swap with the other player
        swapped_cards = []
        self.swapped_cards = swapped_cards

        # Prompt user to enter number of cards they want to swap with the other player
        card_number = 0
        while card_number == 0:
            try:
                card_number = int(
                    input(f"{self.name}, how many cards would you like to swap with {other_player.name}?: "))
                # Check that the number of cards to swap is not greater than the number of cards in the player's hand
                if card_number > len(self.hand):
                    print(
                        "You don't have that many cards in your hand. Please enter a number between 1 and {}".format(
                            len(self.hand)))
                    card_number = 0
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Loop until the player has swapped the specified number of cards
        while len(self.swapped_cards) < card_number:
            # Print the cards in the player's hand along with a number for each card
            print(f"{self.name}'s hand:")
            for i, card in enumerate(self.hand):
                print(f"{i + 1}. {card}")

            # Prompt the player to enter the number corresponding to the card they want to swap
            choice = input("Enter the number of the card you want to swap: ")

            try:
                # Convert the choice to an integer
                choice = int(choice)

                # Check if the choice is a valid number
                if choice >= 1 and choice <= len(self.hand):
                    # Use the choice to get the card from the player's hand and remove it
                    card = self.hand[choice - 1]
                    self.hand.remove(card)

                    # Add the card to the swapped_cards list
                    self.swapped_cards.append(card)

                    print(f"{self.name} will swap the {card}")

                else:
                    print("Invalid choice. Please enter a number between 1 and {}".format(len(self.hand)))
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Draw new cards from the other player's hand and add them to the player's hand
        for i in range(card_number):
            index = random.randint(0, len(other_player.hand) - 1)
            card = other_player.hand.pop(index)
            self.hand.append(card)

        # Add the cards from the swapped_cards list to the other player's hand
        for card in self.swapped_cards:
            other_player.hand.append(card)

    def swap_cards_deck(self):
            # List of cards to swap into deck
            swapped_cards = []
            self.swapped_cards = swapped_cards

            # Prompt user to enter number of cards they want to swap with the deck
            card_number = 0
            while card_number == 0:
                try:
                    card_number = int(input(f"{self.name}, how many cards would you like to swap with the deck?: "))
                    # Check that the number of cards to swap is not greater than the number of cards in the player's hand
                    if card_number > len(self.hand):
                        print(
                            "You don't have that many cards in your hand. Please enter a number between 1 and {}".format(
                                len(self.hand)))
                        card_number = 0
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Loop until the player has swapped the specified number of cards
            while len(self.swapped_cards) < card_number:
                # Print the cards in the player's hand along with a number for each card
                print(f"{self.name}'s hand:")
                for i, card in enumerate(self.hand):
                    print(f"{i + 1}. {card}")

                # Prompt the player to enter the number corresponding to the card they want to swap
                choice = input("Enter the number of the card you want to swap: ")

                try:
                    # Convert the choice to an integer
                    choice = int(choice)

                    # Check if the choice is a valid number
                    if choice >= 1 and choice <= len(self.hand):
                        # Use the choice to get the card from the hand list and remove it
                        card = self.hand[choice - 1]
                        self.hand.remove(card)

                        # Add the card to the swapped_cards list
                        self.swapped_cards.append(card)

                        print(f"{self.name} will swap the {card}")

                    else:
                        print("Invalid choice. Please enter a number between 1 and {}".format(len(self.hand)))
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Draw new cards and add them to the player's hand
            for card in swapped_cards:
                self.deck.append(card)
            for i in range(card_number):
                index = random.randint(0, len(self.deck) - 1)
                card = self.deck.pop(index)
                self.hand.append(card)

    def mulligan(self):
        # create a new empty list to store player's new hand of cards
        new_hand = []

        # add current hand back to deck
        for i in self.hand:
            self.deck.append(i)

        # draw new hand of cards from deck
        for card in range(len(self.hand)):
            index = random.randint(0, len(self.deck) - 1)
            card = self.deck.pop(index)
            new_hand.append(card)

        # set players hand to the new hand of cards
        self.hand = new_hand
        print(f"{self.name} took a mulligan and drew a new hand\n")

    # check to see how many cards are left in deck
    @staticmethod
    def inspect_deck():
        print(f"There are {len(deck)} cards left in the deck.")

    def mill(self, num_milled):
        # use a for loop to remove cards from the deck
        for i in range(num_milled):
            index = random.randint(0, len(self.deck) - 1)
            # use pop method to remove the card at specified index from the deck
            card = self.deck.pop(index)
            # add card to removed_cards list
            self.removed_cards.append(card)

        print(f"{self.name} milled {num_milled} cards\n")

    # Flip a coin
    def coinflip(self):
        coin = ['Heads', 'Tails']
        print(f"{self.name} flipped a coin and it came up {random.choice(coin)}\n")

    def diceroll(self, sides=6, num_of_dice=1):
        # roll a die with X number of sides and print the outcome
        counter = 0
        while counter != num_of_dice:
            droll_outcome = random.randint(1, sides)
            print(f"{self.name} rolled a {droll_outcome}")
            self.rolled_dice.append(droll_outcome)
            counter += 1


    # view most recent dice roll
    def view_rolled_dice(self):
        print(f"{self.name} last rolled {self.rolled_dice}\n")

    def draw_card(self):
        # Generate a random index for the card that you want to remove
        index = random.randint(0, len(self.deck) - 1)

        # Use the pop method to remove the card at the specified index from the deck
        card = self.deck.pop(index)

        # Add the card to the removed_cards list
        self.hand.append(card)
        # Return the card that was drawn
        print(f"{self.name} drew the {card}")
        return card

    def discard_card(self):
        # Print the cards in the player's hand along with a number for each card
        print(f"{self.name}'s hand:")
        for i, card in enumerate(self.hand):
            print(f"{i + 1}. {card}")

        # Loop until the player enters a valid choice
        while True:
            try:
                # Prompt the player to enter the number corresponding to the card they want to discard
                choice = input("Enter the number of the card you want to discard: ")

                # Convert the choice to an integer
                choice = int(choice)

                # Check if the choice is a valid number
                if choice >= 1 and choice <= len(self.hand):
                    # Use the choice to get the card from the hand list and remove it
                    card = self.hand[choice - 1]
                    self.hand.remove(card)

                    # Add the card to the removed_cards list
                    self.removed_cards.append(card)

                    print(f"{self.name} discarded the {card}")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and {}".format(len(self.hand)))
            except:
                ValueError


    def discard_multiple_cards(self, num_cards):
        # Print the cards in the player's hand along with a number for each card
        print(f"{self.name}'s hand:")
        for i, card in enumerate(self.hand):
            print(f"{i + 1}. {card}")

        discarded_cards = []

        # Loop until the player has discarded the specified number of cards
        while len(discarded_cards) < num_cards:
            try:
                # Prompt the player to enter the number corresponding to the card they want to discard
                print("\n")
                choice = input("Enter the number of the card you want to discard: ")

                # Convert the choice to an integer
                choice = int(choice)

                # Check if the choice is a valid number
                if choice >= 1 and choice <= len(self.hand):
                    # Use the choice to get the card from the hand list and remove it
                    card = self.hand[choice - 1]
                    self.hand.remove(card)
                    print(f"{self.name} discarded the {card} \n")

                    # Add the card to the discarded_cards and removed_cards lists
                    discarded_cards.append(card)
                    self.removed_cards.append(card)

                    # Print the cards in the player's hand along with a number for each card
                    print(f"{self.name}'s hand:")
                    for i, card in enumerate(self.hand):
                        print(f"{i + 1}. {card}")

                else:
                    print("Invalid choice. Please enter a number between 1 and {}".format(len(self.hand)))
            except:
                ValueError

        # Print the discarded cards
        print(f"{self.name} discarded the following cards:")
        print(discarded_cards)


    def draw_multiple_cards(self, num_cards):
        # Draw multiple cards from the deck and return them as a list
        drawn_cards = []
        for _ in range(num_cards):
            drawn_card = self.draw_card()
            drawn_cards.append(drawn_card)
        return drawn_cards


    def show_hand(self):
        # Print the cards that the player currently has in their hand
        print(f"{self.name}'s hand:")
        print(self.hand)


    def play_card(self):

        # check if the player has any cards in their hand
        if len(self.hand) == 0:
            print("You have no cards in your hand.")
            return

        # print the cards in players hand with a number for each card
        print(f"{self.name}'s {self.hand}")
        for i, card in enumerate(self.hand):
            print(f"{i + 1}. {card}")

        # Loop until the player enters a valid choice
        while True:
            try:
                # Prompt the player to enter a number corresponding to the card they want to play
                choice = input("Enter the number of the card you want to play: ")

                # convert the choice to an integer
                choice = int(choice)

                # check if choice is a valid number
                if choice >= 1 and choice <= len(self.hand):
                    # use the choice to get the card from the hand list and remove it
                    card = self.hand[choice - 1]
                    self.hand.remove(card)

                    # add card to cards in play on board
                    self.board.cards_in_play.append(card)

                    print(f"{self.name} played the {card}")
                    return card
                else:
                    print("invalid choice please enter a number between 1 and {}".format(len(self.hand)))
            except:
                ValueError


player1 = Player("Human", deck, removed_cards)
player2 = Player("Computer", deck, removed_cards)
