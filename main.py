import socket
import threading

LOCALHOST_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050

HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"

localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TODO: make this idiot-proof
recipient_ip = input("IP Address: ")

def ReceiveMessage(connection, address):
    localhost.bind((LOCALHOST_IP, PORT))
    while True:
        message_len = connection.recv(HEADER).decode(FORMAT)
        if message_len:
            message_len = int(message_len)
            message = connection.recv(message_len).decode(FORMAT)

            if message == DISCONNECT_MESSAGE:
                break

            print(f"<{address}>: {message}")
    connection.close()

def SendMessage(message):
    localhost.connect((recipient_ip, PORT))
    message = message.encode(FORMAT)
    message_length = str(len(message)).encode(FORMAT)
    message_length += b' ' * (HEADER - len(message_length))
    localhost.send(message_length)
    localhost.send(message)
    localhost.close()

localhost.listen()
while True:
    SendMessage(input("Enter your message: "))
    connection, address = localhost.accept()
    thread = threading.Thread(target=ReceiveMessage, args=(connection, address))
    thread.start()
    