import constants


class Message:
    def __init__(self, players):
        self.players = players

    def broadcast(self, message):
        for player in self.players:
            self.send_message(message, player)

    def send_message(self, message, player):
        if type(player) != dict:
            print(type(player))
            for i in self.players:
                if i["name"] == player.name:
                    p_socket = i["socket"]
        else:
            p_socket = player["socket"]
        try:
            p_socket.sendall(message.encode())
        except:
            print(f"Error sending message to {player['name']}")
            self.players.remove(player)

    def choose_card(self, valid_cards, player):
        for i, card in enumerate(valid_cards):
            self.send_message(f"\n{i + 1}. {card}", player)
        self.send_message("\nChoose card: ", player)
        message = self.receive_message(player)
        choice = int(message) - 1
        while choice < 0 or choice >= len(valid_cards):
            self.send_message("Invalid choice. Please try again.", player)
            self.send_message("\nChoose card: ", player)
            message = self.receive_message(player)
            choice = int(message) - 1
        return valid_cards[choice]

    def choose_color(self, player):
        valid_colors = constants.CARD_COLORS
        for i, color in enumerate(valid_colors):
            self.send_message(f"\n{i + 1}. {color}", player)
        self.send_message("\nChoose color: ", player)
        message = self.receive_message(player)
        choice = int(message) - 1
        while choice < 0 or choice >= len(valid_colors):
            self.send_message("Invalid choice. Please try again.", player)
            self.send_message("\nChoose color: ", player)
            message = self.receive_message(player)
            choice = int(message) - 1
        return valid_colors[choice]

    def receive_message(self, player):
        while True:
            try:
                if type(player) != dict:
                    print(type(player))
                    for i in self.players:
                        if i["name"] == player.name:
                            p_socket = i["socket"]
                else:
                    p_socket = player["socket"]
                data = p_socket.recv(1024)
                message = data.decode()
                return message
            except:
                print(f"Error receiving message from {player['name']}")
                self.players.remove(player)
                break
