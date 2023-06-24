import socket
import threading
import atexit
import utility as util

class Sender:
    def __init__(self, ShowMessageFunc):
        self.connected = False
        self.ShowMessage = ShowMessageFunc
        self.localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        atexit.register(self.Disconnect) # If the user exits send a disconnect message

    def SendData(self, length, data):
        # First send a message defining the length of the actual message
        self.localhost.send(length)
        self.localhost.send(data)

    def SendMessage(self, message, showLocally = True):
        try:
            # Show it in the entry box
            if showLocally:
                self.ShowMessage(message)

            message = message.encode(util.FORMAT)

            message_length = str(len(message)).encode(util.FORMAT)
            message_length += b' ' * (util.HEADER - len(message_length))

            sendThread = threading.Thread(target=self.SendData, args=(message_length, message))
            sendThread.start()
            
        except Exception as e:
            self.ShowMessage(str(e))

    def Connect(self, ip):
        try:
            self.localhost.connect((ip, util.PORT))
            self.connected = True

            self.ShowMessage(f"Connected to {ip}")
            self.SendMessage(util.JOINED_MESSAGE, False)
        except Exception as e:
            self.ShowMessage(str(e))

    def Disconnect(self):
        if self.connected:
            self.SendMessage(util.DISCONNECT_MESSAGE)

    def Start(self, ip):
        self.ShowMessage("Connecting...")
        
        # Handle connecting on a separate thread, so the program still responds while connecting
        connectThread = threading.Thread(target=lambda: self.Connect(ip))
        connectThread.start()
        