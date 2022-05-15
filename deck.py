from card import Card
import random

class Deck(object):

    def __init__(self):
        self.cards = []
    
    def draw_card(self):
        return self.cards.pop(0)

    def add_card(self, card):
        self.cards.append(card)

    def add_cards(self, cards):
        self.cards = cards
    
    def shuffle_deck(self):
        random.shuffle(self.cards)