import socket


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connection successful!")
        except socket.error as e:
            print(str(e))

    def send_message(self, message):
        self.client_socket.sendall(message.encode())

    def receive_message(self):
        message = self.client_socket.recv(1024)
        return message.decode()

    def close_connection(self):
        self.client_socket.close()


if __name__ == '__main__':
    host = input("Enter host: ")
    port = 5050
    client = Client(host, port)
    client.connect()
    # message = input("Enter message: ")
    # client.send_message(message)
    response = client.receive_message()
    print(f"Response from server: {response}")
    client.close_connection()
