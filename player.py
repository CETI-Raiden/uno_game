import constants


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand



    def play_card(self, card):
        self.hand.remove(card)
        return card

    def draw_card(self, card):
        self.hand.append(card)

    def has_cards(self):
        return len(self.hand) > 0

    def remove_cards(self, cards):
        for card in cards:
            self.hand.remove(card)

    def add_cards(self, cards, initial_cards=True):
        self.hand += cards
        if initial_cards:
            initial_cards = False
        else:
            print(f"{self.name} has drawn {len(cards)} cards:")
            for card in cards:
                print(f"\t{card}")

    def __str__(self):
        return f"{self.name}: {[str(card) for card in self.hand]}"
