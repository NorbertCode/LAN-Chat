import socket
import threading
import utility as util

class Receiver:
    def __init__(self, ShowMessageFunc):
        self.ShowMessage = ShowMessageFunc
        self.localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.localhost.bind(('0.0.0.0', util.PORT))

    def ReceiveMessage(self, connection, address):
        while True:
            try:
                message_len = connection.recv(util.HEADER).decode(util.FORMAT)
                message_len = int(message_len)

                message = connection.recv(message_len).decode(util.FORMAT)
                if message == util.DISCONNECT_MESSAGE:
                    break
                
                if message == util.JOINED_MESSAGE:
                    self.ShowMessage(f"{address[0]} has joined")
                    break

                self.ShowMessage(f"<{address[0]}>: {message}")
            except:
                self.ShowMessage(f"Connection with {address[0]} has been lost")
                break
                
        connection.close()

    def Start(self):
        self.localhost.listen()
        while True:
            try:
                connection, address = self.localhost.accept()
                thread = threading.Thread(target=self.ReceiveMessage, args=(connection, address))
                thread.start()
            except Exception as e:
                self.ShowMessage(str(e))