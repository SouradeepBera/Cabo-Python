import card
import player
import deck
import json

def initialise_full_deck():
    all_cards = []

    numbers = [str(i) for i in range(2, 11)]
    numbers.extend(["A", "J", "Q", "K"])
    suits = ["clubs","diamonds","spades","hearts"]

    for suit in suits:
        for number in numbers:
            all_cards.append(card.Card(suit, number))
    
    full_deck = deck.Deck()
    full_deck.add_cards(all_cards)
    full_deck.shuffle_deck()
    return full_deck

def instantiate_players(names):
    players = []
    for name in names:
        players.append(player.Player(name))
    return players

def assign_cards(players, full_deck):
    n_players = len(players)
    for i in range (4*n_players):
        players[i//4].add_card(full_deck.draw_card())

    unseen_deck = deck.Deck()
    unseen_cards = [c for c in full_deck.cards]
    unseen_deck.add_cards(unseen_cards)
    unseen_deck.shuffle_deck()
    return unseen_deck

def construct_message(body, response_req=True):
    mssg = {
        'body': body,
        'response_req': response_req
    }
    return json.dumps(mssg, separators=(',', ':'))

def get_input(sub, req_ch):
    for message in sub.listen():
        data = message['data']
        channel = message['channel']
        if channel == req_ch:
            return data
