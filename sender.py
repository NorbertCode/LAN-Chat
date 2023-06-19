import socket
import atexit
import utility as util

def SendMessage(message):
    # First send a message defining the length of the actual message
    message = message.encode(util.FORMAT)

    message_length = str(len(message)).encode(util.FORMAT)
    message_length += b' ' * (util.HEADER - len(message_length))

    localhost.send(message_length)
    localhost.send(message)

def Disconnect():
    SendMessage(util.DISCONNECT_MESSAGE)

localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
atexit.register(Disconnect) # If the user exits send a disconnect message

def Start():
    # Loop this, so if you disconnect or lose connection you can try again
    while True:
        # TODO: make this idiot-proof
        recipient_ip = input("IP Address: ")
        
        localhost.connect((recipient_ip, util.PORT))
        while True:
            try:
                SendMessage(input("Enter your message: "))
            except:
                print("An error occured while trying to reach the destination.")
                break

if __name__ == '__main__':
    Start()