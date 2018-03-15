

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def display(self):
        print('{} of {}'.format(self.rank, self.suit))

    def score(self):
        if self.rank == 'Ace':
            return 11
        if self.rank == 'King' or self.rank == 'Queen' or self.rank == 'Jack':
            return 10
        return int(self.rank)