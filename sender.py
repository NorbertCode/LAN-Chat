import socket
import utility as util

localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def SendMessage(message):
    message = message.encode(util.FORMAT)
    message_length = str(len(message)).encode(util.FORMAT)
    message_length += b' ' * (util.HEADER - len(message_length))
    localhost.send(message_length)
    localhost.send(message)

def Start():
    # TODO: make this idiot-proof
    recipient_ip = input("IP Address: ")
    localhost.connect((recipient_ip, util.PORT))
    while True:
        SendMessage(input("Enter your message: "))