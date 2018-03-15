

class Person:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def take_card(self, card):
        self.cards.append(card)

    def score(self):
        aces = 0
        score = 0
        for card in self.cards:
            if card.score() == 11:
                aces += 1
            score += card.score()
        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score

    def show_cards(self):
        for card in self.cards:
            card.display()

    def show_position(self):
        print('Cards:')
        self.show_cards()
        print('Score:')
        print(self.score())

    def drop_cards(self):
        self.cards = []
