import threading
import receiver
import sender

receiverThread = threading.Thread(target=receiver.Start)
receiverThread.start()
senderThread = threading.Thread(target=sender.Start)
senderThread.start()
