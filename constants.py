# constants.py

CARD_COLORS = ["Red", "Blue", "Green", "Yellow"]
CARD_VALUES = [str(i) for i in range(10)]
CARD_SPECIAL_VALUES = ["Skip", "Reverse", "+2"]
# CARD_POINTS = {str(i): i for i in range(10)}
# CARD_POINTS.update({"Skip": 20, "Reverse": 20, "+2": 20})
WILD_CARDS = ["Color", "+4"]
# WILD_CARD_POINTS = {"Wild": 50, "Wild_+4": 50}
NUMBER_OF_NORMAL_CARDS = 2
NUMBER_OF_SPECIAL_CARDS = 2
NUMBER_OF_WILD_CARDS = 4

MAX_PLAYERS = int(input("Enter number of players (2-10): "))
HAND_SIZE = 7

# Constants for game server

HOST = 'localhost'
PORT = 5050
