from person import Person

class Strategy:

    def __init__(self, score):
        self.score = score


    def take_new_card(self, player):

        # do logic here
        if player.score() >= self.score:
            return False
        return True