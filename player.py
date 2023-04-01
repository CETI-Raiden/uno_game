import constants

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def choose_card(self, valid_cards):
        # if isinstance(current_card, list):
        #     valid_cards = [card for card in self.hand if any(card.is_playable_on(c) for c in current_card)]
        # else:
        #     valid_cards = [card for card in self.hand if card.is_playable_on(current_card)]
        for i, card in enumerate(valid_cards):
            print(f"{i + 1}. {card}")
        choice = int(input("Enter card number: ")) - 1
        while choice < 0 or choice >= len(valid_cards):
            print("Invalid choice. Please try again.")
            choice = int(input("Enter card number: ")) - 1
        return valid_cards[choice]

    def choose_color(self):
        valid_colors = constants.CARD_COLORS
        for i, color in enumerate(valid_colors):
            print(f"{i + 1}. {color}")
        choice = int(input("Enter chosen color: ")) - 1
        while choice < 0 or choice >= len(valid_colors):
            print("Invalid choice. Please try again.")
            choice = int(input("Enter chosen color: ")) - 1
        return valid_colors[choice]

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
