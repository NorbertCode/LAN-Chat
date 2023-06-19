import threading
import tkinter as tk
import receiver
import sender

# Create the main window
root = tk.Tk()
root.geometry("400x500")

# Create an entry box to type messages
ip_field = tk.Entry(root, width=50)
ip_field.pack(pady=10)

# Create a button to send messages
connect_button = tk.Button(root, text="Connect", command=lambda: sender.Start(ip_field.get()), width=10)
connect_button.pack()

# Create a text box to display messages
messages = tk.Text(root, state="disabled", height=20, width=50)
messages.pack(pady=10)

# Create an entry box to type messages
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Function to write content into textbox
def EnterMessage(message):
    messages.configure(state="normal")
    messages.insert("end", message + "\n")
    messages.configure(state="disabled")
    entry.delete(0, "end")

def SendMessage():
    EnterMessage(entry.get())
    sendThread = threading.Thread(target=lambda: sender.SendMessage(entry.get()))
    sendThread.start()

# Create a button to send messages
send_button = tk.Button(root, text="Send", command=SendMessage, width=10)
send_button.pack()

# Start this in a thread so you can receive and send at the same time
receiver.SetOnReceive(EnterMessage)
receiverThread = threading.Thread(target=receiver.Start)
receiverThread.start()

# Run the app
root.mainloop()