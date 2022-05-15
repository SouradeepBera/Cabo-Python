import utils 

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

    def display_all_cards(self, r, ch):
        r.publish(ch , utils.construct_message('Displaying all cards ', False))

        for card in self.cards:
            r.publish(ch , utils.construct_message(str(card), False))
        
    def display_first_two_cards(self, r, ch):
        r.publish(ch , utils.construct_message('Displaying first two cards ', False))

        for card in self.cards[:2]:
            r.publish(ch , utils.construct_message(str(card), False))

    def display_card_by_idx(self, idx, r, ch):
        r.publish(ch , utils.construct_message("Displaying card for player at index"+str(idx), False))
        r.publish(ch , utils.construct_message(str(self.cards[idx]), False))