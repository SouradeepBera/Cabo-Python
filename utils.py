from card import Card
from player import Player
from deck import Deck

def initialise_full_deck():
    all_cards = []

    numbers = [str(i) for i in range(2, 11)]
    numbers.extend(["A", "J", "Q", "K"])
    suits = ["clubs","diamonds","spades","hearts"]

    for suit in suits:
        for number in numbers:
            all_cards.append(Card(suit, number))
    
    full_deck = Deck()
    full_deck.add_cards(all_cards)
    full_deck.shuffle_deck()
    return full_deck

def instantiate_players(names):
    players = []
    for name in names:
        players.append(Player(name))
    return players

def assign_cards(players, full_deck):
    n_players = len(players)
    for i in range (4*n_players):
        players[i//4].add_card(full_deck.draw_card())

    unseen_deck = Deck()
    unseen_cards = [c for c in full_deck.cards]
    unseen_deck.add_cards(unseen_cards)
    unseen_deck.shuffle_deck()
    return unseen_deck
