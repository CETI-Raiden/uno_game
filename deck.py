import random
from card import Card, Color, DrawFour, Skip, PlusTwo, Reverse
import constants


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for color in constants.CARD_COLORS:
            # Add normal cards
            for value in constants.CARD_VALUES:
                # Don't add 0 for wild cards
                if value != "0":
                    for i in range(constants.NUMBER_OF_NORMAL_CARDS):
                        # card_points = constants.CARD_POINTS[value]
                        self.cards.append(Card(color, value))
                else:
                    self.cards.append(Card(color, value))

            # Add special cards
            for value in constants.CARD_SPECIAL_VALUES:
                for i in range(constants.NUMBER_OF_SPECIAL_CARDS):
                    # card_points = constants.CARD_POINTS[value]
                    # self.cards.append(Card(color, value))
                    if value == constants.CARD_SPECIAL_VALUES[0]:
                        self.cards.append(Skip(color))
                    elif value == constants.CARD_SPECIAL_VALUES[1]:
                        self.cards.append(Reverse(color))
                    elif value == constants.CARD_SPECIAL_VALUES[2]:
                        self.cards.append(PlusTwo(color))

            # Add wild cards
        for value in constants.WILD_CARDS:
            for i in range(constants.NUMBER_OF_WILD_CARDS):
                # card_points = constants.WILD_CARD_POINTS[value]
                # self.cards.append(WildCard(value))
                if value == constants.WILD_CARDS[0]:
                    self.cards.append(Color(value))
                elif value == constants.WILD_CARDS[1]:
                    self.cards.append(DrawFour(value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None

    def draw_cards(self, num_cards):
        cards = []
        for i in range(num_cards):
            card = self.draw_card()
            if card is not None:
                cards.append(card)
        return cards
