import socket
import utility as util

# TODO: make this idiot-proof
recipient_ip = input("IP Address: ")

localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost.connect((recipient_ip, util.PORT))

def SendMessage(message):
    message = message.encode(util.FORMAT)
    message_length = str(len(message)).encode(util.FORMAT)
    message_length += b' ' * (util.HEADER - len(message_length))
    localhost.sendto(message_length, (recipient_ip, util.PORT))
    localhost.sendto(message, (recipient_ip, util.PORT))

localhost.listen()
while True:
    SendMessage(input("Enter your message: "))
    