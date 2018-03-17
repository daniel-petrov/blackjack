from card import Card
from random import shuffle

class Deck:

    def __init__(self):
        self.ranks = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        # self.deck = []
        # for suit in self.suits:
        #     for rank in self.ranks:
        #         card = Card(suit, rank)
        #         self.deck.append(card)

        # do the same what's above using list comprehension
        self.deck = [Card(suit=i, rank=j) for i in self.suits for j in self.ranks]
        
        # print([i.display() for i in self.deck])

    def shuffle(self):
        shuffle(self.deck)

    def next_card(self):
        return self.deck.pop()

    def cards_left(self):
        return len(self.deck)
