import threading
import receiver
import sender

# Start each of these on seperate threads, so you can receive and send messages at the same time
receiverThread = threading.Thread(target=receiver.Start)
receiverThread.start()
senderThread = threading.Thread(target=sender.Start)
senderThread.start()
