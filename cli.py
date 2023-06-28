import threading
import receiver
import sender

if __name__ == "__main__":
    receive = receiver.Receiver(print)
    receiverThread = threading.Thread(target=receive.Start, daemon=True)
    receiverThread.start()

    ip = input("Enter the IP you want to connect to: ")
    send = sender.Sender(print)
    send.Start(ip)

    def MessageInput():
        while True:
            send.SendMessage(input("> "))

    sendingThread = threading.Thread(target=MessageInput)
    sendingThread.start()