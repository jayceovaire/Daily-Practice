import random
from random import *

def lottery():
    prompt = input("Press 'Enter' to get your ticket and start the lottery")
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print(prompt)
    my_ticket = str(choice(values))
    counter = 0
    pulled_ticket = ""
    while str(my_ticket) != str(pulled_ticket):
        for _ in range(0, 1):
            print(pulled_ticket)
            counter += 1
            pulled_ticket = choice(values)

            if str(my_ticket) == str(pulled_ticket):
                print(pulled_ticket)
                print(f"Your ticket was {my_ticket}!")
                print(f"You won! it only took {counter} tries!")
                return str(pulled_ticket)
lottery()