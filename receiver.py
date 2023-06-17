import socket
import threading
import utility as util

localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost.bind(('0.0.0.0', util.PORT))

def ReceiveMessage(connection, address):
    while True:
        message_len = connection.recv(util.HEADER).decode(util.FORMAT)
        if message_len: # !crashes here when you unexpectedly terminate sender.py
            message_len = int(message_len)
            message = connection.recv(message_len).decode(util.FORMAT)

            if message == util.DISCONNECT_MESSAGE:
                break

            print(f"<{address}>: {message}")
    connection.close()

localhost.listen()
print("[Started Receiving]")
while True:
    connection, address = localhost.accept()
    thread = threading.Thread(target=ReceiveMessage, args=(connection, address))
    thread.start()
    
