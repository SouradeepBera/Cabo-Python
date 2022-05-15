from utils import initialise_full_deck, instantiate_players, assign_cards, construct_message
from card import Card
from player import Player
from deck import Deck
from game import Game
import random
import redis
import json


r = redis.Redis(host="redis-19760.c212.ap-south-1-1.ec2.cloud.redislabs.com", port=19760,
                username="Server", password="Server@123", decode_responses=True)

sub = r.pubsub(ignore_subscribe_messages=True)



r.publish("server-to-all" , construct_message('enter name: '))
n_players = r.execute_command('PUBSUB', 'NUMSUB', 'server-to-all')[1]

names = [0]*n_players

for i in range(n_players):
    sub.subscribe("client"+str(i)+"-to-server")

rsum = 0
for message in sub.listen():
    data = message['data']
    message['channel'].split('-')
    client_id = int(message['channel'].split('-')[0][6:])
    rsum+=client_id+1
    names[client_id] = data
    if rsum == (n_players*(n_players+1))//2:
        break

players = instantiate_players(names)
r.publish("server-to-all" , construct_message('Players instantiated', False))

full_deck = initialise_full_deck()
unseen_deck = assign_cards(players, full_deck)
r.publish("server-to-all" , construct_message('Cards assigned', False))

for i in range(n_players):
    p = players[i]
    ch = "server-to-client" + str(i)
    p.display_first_two_cards(r, ch)

starting_player_idx = random.randint(0, n_players-1)
idx = starting_player_idx
r.publish("server-to-all" , construct_message('Game starting with'+str(players[idx]), False))

game = Game(players, unseen_deck, r, sub)
while idx != -1:
    idx = game.play(idx)
