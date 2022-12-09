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


class Player:
    def __init__(self, name, deck, removed_cards):
        self.name = name
        # Accept the deck and removed_cards lists as arguments and store them as instance variables
        self.deck = deck
        self.removed_cards = removed_cards
        self.hand = []

    def draw_card(self):
        # Generate a random index for the card that you want to remove
        index = random.randint(0, len(self.deck) - 1)

        # Use the pop method to remove the card at the specified index from the deck
        card = self.deck.pop(index)

        # Add the card to the removed_cards list
        self.hand.append(card)
        self.removed_cards.append(card)
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
            except: ValueError


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

player1 = Player("Josh", deck, removed_cards)
player2 = Player("Computer", deck, removed_cards)

player1.draw_multiple_cards(5)
player1.show_hand()
player1.discard_card()
player1.show_hand()