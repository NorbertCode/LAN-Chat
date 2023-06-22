import socket
import threading
import utility as util

class Receiver:
    def __init__(self, ShowMessageFunc):
        self.ShowMessage = ShowMessageFunc
        self.localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.localhost.bind(('0.0.0.0', util.PORT))

    def ReceiveMessage(self, connection, address, onReceive):
        while True:
            try:
                message_len = connection.recv(util.HEADER).decode(util.FORMAT)
                message_len = int(message_len)

                message = connection.recv(message_len).decode(util.FORMAT)
                if message == util.DISCONNECT_MESSAGE:
                    break
                
                onReceive(f"<{address[0]}>: {message}")
            except:
                onReceive(f"Connection with {address[0]} has been lost")
                break
                
        connection.close()

    def Start(self):
        self.localhost.listen()
        while True:
            try:
                connection, address = self.localhost.accept()
                thread = threading.Thread(target=self.ReceiveMessage, args=(connection, address, self.ShowMessage))
                thread.start()
            except:
                self.ShowMessage("An error has occured")