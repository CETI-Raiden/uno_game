import socket
import threading
from constants import HOST, PORT, MAX_PLAYERS


class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOST, PORT))
        self.sock.listen()
        self.players = []

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        player = conn.recv(1024).decode()
        self.players.append(player)
        print(f"[ACTIVE CONNECTIONS] {len(self.players)} players connected.")
        if len(self.players) == MAX_PLAYERS:
            self.start_game()
        conn.close()

    def start_game(self):
        print("Starting game...")
        # Game logic goes here

    def run(self):
        print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
        while True:
            conn, addr = self.sock.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} players connected.")


if __name__ == '__main__':
    server = Server()
    server.run()
