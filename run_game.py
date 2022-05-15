from utils import initialise_full_deck, instantiate_players, assign_cards
from card import Card
from player import Player
from deck import Deck
from game import Game
import random

names = input("Enter names: ")
names = names.split()
n_players = len(names)

players = instantiate_players(names)
print("Players instantiated")

full_deck = initialise_full_deck()
unseen_deck = assign_cards(players, full_deck)
print("Cards assigned")

for p in players:
    p.display_first_two_cards()

starting_player_idx = random.randint(0, n_players-1)
idx = starting_player_idx
print('Game starting with', players[idx])

game = Game(players, unseen_deck)
while idx != -1:
    idx = game.play(idx)
