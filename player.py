from card import Card

class Player(object):

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.blocked = []
    
    def __str__(self):
        return self.name

    def add_card(self, card):
        self.cards.append(card)
        self.blocked.append(0)
    
    def block_card(self, idx):
        self.blocked[idx] = 1
    
    def get_card_by_idx(self, idx):
        return self.cards[idx]

    def replace_card(self, new_card, idx):
        old_card = self.cards[idx]
        self.cards[idx] = new_card
        return old_card

    def display_all_cards(self):
        print("Displaying all cards for player", self.name)
        for card in self.cards:
            print(card)
        
    def display_first_two_cards(self):
        print("Displaying first two cards for player", self.name)
        for card in self.cards[:2]:
            print(card)

    def display_card_by_idx(self, idx):
        print("Displaying card for player", self.name, "at index", idx)
        print(self.cards[idx])