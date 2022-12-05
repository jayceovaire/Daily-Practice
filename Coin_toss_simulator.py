import random

# Coin Toss Simulator


class Coin:
    def __init__(self):
        pass

    @staticmethod
    def toss(num_tosses=1):
        # results tallies outcomes of flips stored in outcomes list.
        results = {'Heads': 0, 'Tails': 0}
        possibilties = ['Heads', 'Tails']
        outcomes = []
        # counter is equal to number of times you want to flip coin
        counter = int(num_tosses)

        while counter != 0:
            # Flips coin number of times as input (num_tosses)
            outcome = random.choice(possibilties)
            outcomes.append(outcome)
            counter -= 1
        # total flips reduced by one and outcome recorded in outcomes
        # flip outcomes are tallied in results list above.

        for i in outcomes:
            if i == 'Heads':
                results[i] = results.get(i, 0) + 1
            if i == 'Tails':
                results[i] = results.get(i, 0) + 1

        # Display results of Heads and Tails
        for key, value in results.items():
            print(key, ":", value)
