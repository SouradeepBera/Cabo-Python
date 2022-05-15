from card import Card
from player import Player
from deck import Deck

class Game(object):

    def __init__(self, players, unseen_deck):
        self.players = players
        self.unseen_deck = unseen_deck
        self.seen_deck = Deck()

    def terminate(self):
        print("\nTerminating Game")
        for p in self.players:
            p.display_all_cards()

    def play(self, p_idx):
        print("Current player:", self.players[p_idx])

        kaboo = int(input("Kaboo? 1 or 0: "))
        if kaboo:
            self.terminate()
            return -1
        
        drawn_card = self.unseen_deck.draw_card()
        put_card = drawn_card

        print("Drawn card:", drawn_card)

        swap_card = int(input("Swap card? 1 or 0: "))
        if swap_card:
            c_idx = int(input("Enter idx of card you want to swap with: "))
            put_card = self.players[p_idx].replace_card(drawn_card, c_idx)
        
        self.seen_deck.add_card(put_card)
        print("Card on top of seen deck", put_card)

        # TODO: Timer logic

        # power card logic
        if put_card.number == '7' or put_card.number == '8':
            diplay_card_idx = int(input("Enter own card index: "))
            display_card = self.players[p_idx].get_card_by_idx(diplay_card_idx)
            print("Displaying own card:", display_card)
        
        elif put_card.number == '9' or put_card.number == '10':
            opponent_idx = int(input("Enter opponent index: "))
            diplay_card_idx = int(input("Enter oppenent's card index: "))
            display_card = self.players[opponent_idx].get_card_by_idx(diplay_card_idx)
            print("Displaying opponent card:", display_card)
        
        elif put_card.number == 'J':
            p_idx += 1
            p_idx = p_idx % len(self.players)
            print("Skipping player", self.players[p_idx])
        
        elif put_card.number == 'Q':
            opponent_idx = int(input("Enter opponent index: "))
            opponent_card_idx = int(input("Enter oppenent's card index: "))
            player_card_idx = int(input("Enter own card index: "))
            
            opponent_card = self.players[opponent_idx].get_card_by_idx(opponent_card_idx)
            player_card = self.players[p_idx].get_card_by_idx(player_card_idx)

            _ = self.players[p_idx].replace_card(opponent_card, player_card_idx)
            _ = self.players[opponent_idx].replace_card(player_card, opponent_card_idx)

            print("Swapped cards between", self.players[opponent_idx], 'and', self.players[p_idx])

        elif put_card.number == 'K':
            opponent_idx = int(input("Enter opponent index: "))
            opponent_card_idx = int(input("Enter oppenent's card index: "))
            player_card_idx = int(input("Enter own card index: "))
            
            opponent_card = self.players[opponent_idx].get_card_by_idx(opponent_card_idx)
            player_card = self.players[p_idx].get_card_by_idx(player_card_idx)

            print("Displaying opponent card:", opponent_card)
            print("Displaying own card:", player_card)

            to_swap = int(input("Swap card? 1 for Y, 0 for N: "))

            if to_swap:
                _ = self.players[p_idx].replace_card(opponent_card, player_card_idx)
                _ = self.players[opponent_idx].replace_card(player_card, opponent_card_idx)

                print("Swapped cards between", self.players[opponent_idx], 'and', self.players[p_idx])

        p_idx += 1
        p_idx = p_idx % len(self.players)
        return p_idx