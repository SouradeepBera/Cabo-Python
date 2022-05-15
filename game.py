import deck 
import utils


class Game(object):

    def __init__(self, players, unseen_deck, r, sub):
        self.sub = sub
        self.r = r
        self.players = players
        self.unseen_deck = unseen_deck
        self.seen_deck = deck.Deck()

    def terminate(self):
        self.r.publish("server-to-all" , utils.construct_message('Terminating Game', False))
        ch = "server-to-all" 
        for i in range(len(self.players)):
            p = self.players[i]
            p.display_all_cards(self.r, ch)

    def play(self, p_idx):
        all_ch = "server-to-all"
        p_ch = "server-to-client" + str(p_idx)
        server_ch = "client"+str(p_idx)+"-to-server"

        self.r.publish(all_ch , utils.construct_message("Current player:"+ str(self.players[p_idx]), False))

        self.r.publish(p_ch , utils.construct_message("Kaboo? 1 or 0: "))
        
        kaboo = int(utils.get_input(self.sub, server_ch))
        
        if kaboo:
            self.terminate()
            return -1
        
        drawn_card = self.unseen_deck.draw_card()
        put_card = drawn_card

        self.r.publish(p_ch , utils.construct_message("Drawn card:"+ str(drawn_card) + "\nSwap card? 1 or 0: "))

        swap_card = int(utils.get_input(self.sub, server_ch))

        if swap_card:
            self.r.publish(p_ch , utils.construct_message("Enter idx of card you want to swap with: "))
            c_idx = int(utils.get_input(self.sub, server_ch))
            put_card = self.players[p_idx].replace_card(drawn_card, c_idx)
        
        self.seen_deck.add_card(put_card)
        self.r.publish(all_ch , utils.construct_message("Card on top of seen deck"+str(put_card), False))

        # TODO: Timer logic

        # power card logic
        if put_card.number == '7' or put_card.number == '8':
            self.r.publish(p_ch , utils.construct_message("Enter own card index: "))
            diplay_card_idx = int(utils.get_input(self.sub, server_ch))
            display_card = self.players[p_idx].get_card_by_idx(diplay_card_idx)
            self.r.publish(p_ch , utils.construct_message("Displaying own card:"+ str(display_card), False))
        
        elif put_card.number == '9' or put_card.number == '10':
            self.r.publish(p_ch , utils.construct_message("Enter opponent index: "))
            opponent_idx = int(utils.get_input(self.sub, server_ch))
            self.r.publish(p_ch , utils.construct_message("Enter oppenent's card index: "))
            diplay_card_idx = int(utils.get_input(self.sub, server_ch))

            display_card = self.players[opponent_idx].get_card_by_idx(diplay_card_idx)
            self.r.publish(p_ch , utils.construct_message("Displaying opponent's card:"+ str(display_card), False))
        
        elif put_card.number == 'J':
            p_idx += 1
            p_idx = p_idx % len(self.players)
            self.r.publish(all_ch , utils.construct_message("Skipping Player" + str(p_idx), False))
        
        elif put_card.number == 'Q':
            self.r.publish(p_ch , utils.construct_message("Enter opponent index: "))
            opponent_idx = int(utils.get_input(self.sub, server_ch))
            self.r.publish(p_ch , utils.construct_message("Enter oppenent's card index: "))
            opponent_card_idx = int(utils.get_input(self.sub, server_ch))
            self.r.publish(p_ch , utils.construct_message("Enter own card index: "))
            player_card_idx = int(utils.get_input(self.sub, server_ch))

            opponent_card = self.players[opponent_idx].get_card_by_idx(opponent_card_idx)
            player_card = self.players[p_idx].get_card_by_idx(player_card_idx)

            _ = self.players[p_idx].replace_card(opponent_card, player_card_idx)
            _ = self.players[opponent_idx].replace_card(player_card, opponent_card_idx)

            self.r.publish(all_ch , utils.construct_message("Swapped cards between"+ str(self.players[opponent_idx])+ ' and '+ str(self.players[p_idx]), False))

        elif put_card.number == 'K':
            self.r.publish(p_ch , utils.construct_message("Enter opponent index: "))
            opponent_idx = int(utils.get_input(self.sub, server_ch))
            self.r.publish(p_ch , utils.construct_message("Enter oppenent's card index: "))
            opponent_card_idx = int(utils.get_input(self.sub, server_ch))
            self.r.publish(p_ch , utils.construct_message("Enter own card index: "))
            player_card_idx = int(utils.get_input(self.sub, server_ch))
            
            opponent_card = self.players[opponent_idx].get_card_by_idx(opponent_card_idx)
            player_card = self.players[p_idx].get_card_by_idx(player_card_idx)

            self.r.publish(p_ch , utils.construct_message("Displaying opponent card:"+str(opponent_card), False))
            self.r.publish(p_ch , utils.construct_message("Displaying own card:"+str(player_card), False))

            self.r.publish(p_ch , utils.construct_message("Swap card? 1 for Y, 0 for N: "))
            to_swap = int(utils.get_input(self.sub, server_ch))

            if to_swap:
                _ = self.players[p_idx].replace_card(opponent_card, player_card_idx)
                _ = self.players[opponent_idx].replace_card(player_card, opponent_card_idx)

            self.r.publish(all_ch , utils.construct_message("Swapped cards between"+ str(self.players[opponent_idx])+ ' and '+ str(self.players[p_idx]), False))

        p_idx += 1
        p_idx = p_idx % len(self.players)
        return p_idx