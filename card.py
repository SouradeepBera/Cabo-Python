
class Card(object):

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def __eq__(self, other):
        return vars(self) == vars(other)
    
    def __hash__(self):
        return hash((self.suit, self.number))
    
    def __str__(self):
        return self.number + " of " + self.suit
