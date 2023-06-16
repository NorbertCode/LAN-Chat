import socket
import threading

LOCALHOST_IP = "127.0.0.1"
PORT = 5050

HEADER = 64
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "disconnect"

# TODO: make this idiot-proof
recipient_ip = input("IP Address: ")

localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost.bind((LOCALHOST_IP, PORT))

def ReceiveMessage(connection, address):
    while True:
        message_len = connection.recv(HEADER).decode(FORMAT)
        if message_len:
            message_len = int(message_len)
            message = connection.recv(message_len).decode(FORMAT)
            if message == DISCONNECT_MESSAGE:
                break
            
            print(f"<{address}>: {message}")

localhost.listen()
while True:
    connection, address = localhost.accept()
    thread = threading.Thread(target=ReceiveMessage, args=(connection, address))
    thread.start()
    
