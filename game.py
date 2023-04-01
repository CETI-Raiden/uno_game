import constants
from deck import Deck
from player import Player
from card import WildCard


class Game:
    def __init__(self):
        self.num_players = constants.MAX_PLAYERS
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        self.current_player = None
        self.current_card = None
        self.direction = 1
        self.winner = None
        self.initialize_players()

    def initialize_players(self):
        for i in range(self.num_players):
            player_name = input("Enter player name: ")
            self.players.append(Player(player_name, []))

        for i in range(constants.HAND_SIZE):
            for player in self.players:
                player.add_cards([self.deck.draw_card()], initial_cards=True)

        self.current_card = self.deck.draw_card()
        while self.current_card.color == constants.WILD_CARDS[0] or self.current_card.color == constants.WILD_CARDS[1]:
            self.deck.cards.append(self.current_card)
            self.deck.shuffle()
            self.current_card = self.deck.draw_card()

        self.current_player = self.players[0]

    def start(self):
        while self.winner is None:
            print(f"\nCurrent card: {self.current_card}")
            print(f"Current player: {self.current_player}")
            self.play_turn()
            self.check_for_winner()

        print(f"\n{self.winner} wins!")

    def play_turn(self):
        played_card = None
        skip_next_player = False  # flag to skip the next player if a skip card is played
        cumulative_draw_count = 0  # counter for stacking draw cards
        while played_card is None:
            valid_cards = [card for card in self.current_player.hand if card.is_playable_on(self.current_card)]
            if valid_cards:
                played_card = self.current_player.choose_card(valid_cards)
                self.current_player.remove_cards([played_card])
                self.current_card = played_card
                if len(self.current_player.hand) == 1:
                    print("UNO!")
                if isinstance(played_card, WildCard):
                    played_card.color = self.current_player.choose_color()
                if played_card.color == constants.WILD_CARDS[0]:
                    self.deck.cards.append(self.current_card)
                    self.deck.shuffle()
                    self.current_card = self.deck.draw_card()
                if played_card.number == constants.CARD_SPECIAL_VALUES[1]:
                    self.direction = -self.direction
                if played_card.number == constants.CARD_SPECIAL_VALUES[0]:
                    player_idx = self.players.index(self.current_player)
                    skip_next_player = True  # set the flag to skip the next player
                    self.current_player = self.players[player_idx]
                if played_card.number == constants.CARD_SPECIAL_VALUES[2]:
                    next_player = self.get_next_player()
                    next_player.add_cards([self.deck.draw_card() for _ in range(2)])
                if played_card.color == constants.WILD_CARDS[1]:
                    next_player = self.get_next_player()
                    next_player.add_cards([self.deck.draw_card() for _ in range(4)])
                    played_card.color = self.current_player.choose_color()
            else:
                print(f"{self.current_player.name} has no valid cards to play and must draw a card.")
                self.current_player.add_cards([self.deck.draw_card()])
                break

        player_idx = self.players.index(self.current_player)
        player_idx = (player_idx + self.direction) % len(self.players)

        if skip_next_player:
            player_idx = (player_idx + self.direction) % len(self.players)  # skip the next player

        self.current_player = self.players[player_idx]

    def check_for_winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player.name
                break

    def get_next_player(self):
        index = self.players.index(self.current_player)
        index = (index + self.direction) % len(self.players)
        return self.players[index]
