
def pick_card():
    import random
    card_points =['Ace', 'King', 'Queen',
                  'Jack', '2', '3', '4', '5',
                  '6', '7', '8', '9', '10']
    card_signs =['Hearts', 'Clubs', 'Diamonds', 'Spades']
    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    print(f"You chose the {random_point} of {random_sign}.")

pick_card()








