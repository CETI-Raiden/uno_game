import socket
import threading
from game import Game
from constants import MAX_PLAYERS, HOST, PORT
from messages import Message


class Server:
    def __init__(self):
        self.server_socket = None
        self.players = []
        self.names = []
        self.message = None
        self.current_player = None
        self.current_color = None
        self.deck = None
        self.game_direction = None
        self.game_over = False
        self.current_winner = None
        self.turn_index = 0
        self.buffer_size = 2048

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((HOST, PORT))
        self.server_socket.listen(MAX_PLAYERS)
        print(f"Server is listening on {HOST}:{PORT} for a maximum of {MAX_PLAYERS} players")

        while len(self.players) < MAX_PLAYERS:
            client_socket, address = self.server_socket.accept()
            print(f"New connection from {address}")
            player_name = self.get_player_name(client_socket)
            player = {
                "socket": client_socket,
                "name": player_name,
                "hand": []
            }
            self.players.append(player)
            threading.Thread(target=self.receive_message, args=(player,)).start()

        print("All players connected. Starting game.")

        self.message = Message(self.players)

        self.start_game()

    def get_player_name(self, client_socket):
        client_socket.sendall(b"Choose your name:")
        return self.receive_name(client_socket)

    # def send_message(self, message, player):
    #     try:
    #         player["socket"].sendall(message.encode())
    #     except:
    #         print(f"Error sending message to {player['name']}")
    #         self.players.remove(player)
    #
    # def broadcast(self, message):
    #     for player in self.players:
    #         self.send_message(message, player)

    def receive_message(self, player):
        while True:
            try:
                message = player["socket"].recv(self.buffer_size).decode().strip()
                # self.process_message(message, player)
            except:
                print(f"Error receiving message from {player['name']}")
                self.players.remove(player)
                break

    def receive_name(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            message = data.decode()
            if message in self.names:
                client_socket.sendall(b"Name taken, choose again:")
                continue
            else:
                print(f"Player name: ", message)
                self.names.append(message)
                return message

    def start_game(self):
        game = Game(self.players)
        self.message.broadcast("Game is starting!\n")
        game.start_game()
        self.server_socket.close()


# if __name__ == "__main__":
#     server = Server()
#     server.start()
