from game import Game
from server import Server


def test_game():
    # Initialize game with 2 players
    server = Server()
    server.start()


test_game()
