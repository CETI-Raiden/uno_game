import constants


class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
        # self.value = self.get_value()

    # def get_value(self):
    #     if self.color == constants.WILD_CARDS[0] or self.color == constants.WILD_CARDS[1]:
    #         return constants.WILD_CARD_POINTS[self.color]
    #     elif self.color in constants.CARD_COLORS:
    #         if self.number in constants.CARD_POINTS:
    #             return constants.CARD_POINTS[self.number]
    #         else:
    #             raise ValueError("Invalid card number")
    #     else:
    #         raise ValueError("Invalid card color")

    def is_playable_on(self, other_card):
        if self.color == other_card.color:
            return True
        elif isinstance(self, (WildCard, Color, DrawFour)):
            return True
        elif self.number == other_card.number and self.color in constants.CARD_COLORS:
            return True
        elif isinstance(self, Skip) and self.color == other_card.color:
            return True
        elif isinstance(self, Reverse) and self.color == other_card.color:
            return True
        elif isinstance(self, PlusTwo) and (self.color == other_card.color or isinstance(other_card, PlusTwo)):
            return True
        else:
            return False

    def can_chain_draw(self, other_card):
        if isinstance(self, DrawFour):
            return True
        elif isinstance(self, PlusTwo) and (isinstance(other_card, PlusTwo) or other_card.number == "+2"):
            return True
        else:
            return False

    def __str__(self):
        return f"{self.color} {self.number}"


class WildCard(Card):
    def __init__(self, value):
        super().__init__("Wild", value)
        # self.value = constants.WILD_CARD_POINTS[constants.WILD_CARDS[0]]
        # self.allowed_colors = constants.CARD_COLORS

    def __str__(self):
        return f"{self.color} {self.number}"


class DrawFour(WildCard):
    def __init__(self, value):
        super().__init__(value)
        # self.value = constants.WILD_CARD_POINTS[constants.WILD_CARDS[1]]

    def __str__(self):
        return f"{self.color} {self.number}"


class Color(WildCard):
    def __init__(self, value):
        super().__init__(value)
        # self.value = constants.WILD_CARD_POINTS[constants.WILD_CARDS[0]]

    def __str__(self):
        return f"{self.color} {self.number}"


class Skip(Card):
    def __init__(self, color):
        super().__init__(color, constants.CARD_SPECIAL_VALUES[0])
        # self.value = constants.CARD_POINTS["Skip"]
        self.number = constants.CARD_SPECIAL_VALUES[0]

    def __str__(self):
        return f"{self.color} {self.number}"


class Reverse(Card):
    def __init__(self, color):
        super().__init__(color, constants.CARD_SPECIAL_VALUES[1])
        # self.value = constants.CARD_POINTS["Reverse"]
        self.number = constants.CARD_SPECIAL_VALUES[1]

    def __str__(self):
        return f"{self.color} {self.number}"


class PlusTwo(Card):
    def __init__(self, color):
        super().__init__(color, constants.CARD_SPECIAL_VALUES[2])
        # self.value = constants.CARD_POINTS["+2"]
        self.number = constants.CARD_SPECIAL_VALUES[2]

    def __str__(self):
        return f"{self.color} {self.number}"
