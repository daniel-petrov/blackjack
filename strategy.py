from person import Person

class Strategy:

    def __init__(self, threshold):
        self.threshold = threshold


    def take_new_card(self, player):

        # decision making
        if player.score() >= self.threshold:
            return False
        return True