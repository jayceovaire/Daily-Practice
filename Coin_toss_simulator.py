import random

#Coin Toss Simulator

class Coin:
    def __init__(self):
        pass
    def toss(self, num_tosses):
        results = {'Heads': 0, 'Tails': 0}
        possibilties = ['Heads', 'Tails']
        outcomes = []
        counter = int(num_tosses)
        while counter != 0:
            outcome = random.choice(possibilties)
            outcomes.append(outcome)
            counter -= 1
        for i in outcomes:
            if i == 'Heads':
                results[i] = results.get(i, 0) + 1
            if i == 'Tails':
                results[i] = results.get(i, 0) + 1
        print(results)
coin1 = Coin()
coin1.toss(1)
