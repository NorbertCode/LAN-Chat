import socket
import atexit
import utility as util

def SetOnSend(onSendFunc):
    global onSend
    onSend = onSendFunc

def SendMessage(message):
    try:
        # Show it in the entry box
        onSend(message)

        # First send a message defining the length of the actual message
        message = message.encode(util.FORMAT)

        message_length = str(len(message)).encode(util.FORMAT)
        message_length += b' ' * (util.HEADER - len(message_length))

        localhost.send(message_length)
        localhost.send(message)
        
    except:
        onSend("The destination cannot be reached")


def Disconnect():
    SendMessage(util.DISCONNECT_MESSAGE)

localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
atexit.register(Disconnect) # If the user exits send a disconnect message

def Start(ip):
    try:
        localhost.connect((ip, util.PORT))
        onSend(f"Connected to {ip}")
    except:
        onSend("Cannot reach this IP")

if __name__ == '__main__':
    Start()