import socket
import threading
import atexit
import utility as util

class Sender:
    def __init__(self, ShowMessageFunc):
        self.connected = False
        self.ShowMessage = ShowMessageFunc
        atexit.register(self.Disconnect) # If the user exits send a disconnect message

    def SendData(self, length, data):
        try:
            # First send a message defining the length of the actual message
            self.localhost.send(length)
            self.localhost.send(data)
        except Exception as e:
            self.ShowMessage(str(e))

    def SendMessage(self, message, showLocally = True):
        # Show it in the entry box
        if showLocally:
            self.ShowMessage(f"<You>: {message}")

        message = message.encode(util.FORMAT)

        message_length = str(len(message)).encode(util.FORMAT)
        message_length += b' ' * (util.HEADER - len(message_length))

        sendThread = threading.Thread(target=self.SendData, args=(message_length, message))
        sendThread.start()

    def Connect(self, ip):
        if not self.connected:
            try:
                self.localhost.connect((ip, util.PORT))
                self.connected = True

                self.ShowMessage(f"Connected to {ip}")
                self.SendMessage(util.JOINED_MESSAGE, False)
            except Exception as e:
                self.ShowMessage(str(e))

    def Disconnect(self):
        if self.connected:
            self.connected = False
            self.SendMessage(util.DISCONNECT_MESSAGE, False)

            # This throws an error if the disconnect is caused by closing the program
            # In that case you don't need to communicate it locally
            try:
                self.ShowMessage("Disconnecting...")
            except:
                pass

    def Start(self, ip):
        self.ShowMessage("Connecting...")
        self.localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Handle connecting on a separate thread, so the program still responds while connecting
        connectThread = threading.Thread(target=lambda: self.Connect(ip))
        connectThread.start()
        