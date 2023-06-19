import socket
import threading
import utility as util

localhost = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost.bind(('0.0.0.0', util.PORT))

def SetOnReceive(onReceiveFunc):
    global onReceive
    onReceive = onReceiveFunc

def ReceiveMessage(connection, address, onReceive):
    while True:
        message_len = connection.recv(util.HEADER).decode(util.FORMAT)
        if message_len: # !crashes here when you unexpectedly terminate sender.py
            message_len = int(message_len)
            message = connection.recv(message_len).decode(util.FORMAT)

            if message == util.DISCONNECT_MESSAGE:
                break

            onReceive(f"<{address[0]}>: {message}")
    connection.close()

def Start():
    localhost.listen()
    while True:
        connection, address = localhost.accept()
        thread = threading.Thread(target=ReceiveMessage, args=(connection, address, onReceive))
        thread.start()
    
if __name__ == '__main__':
    Start()