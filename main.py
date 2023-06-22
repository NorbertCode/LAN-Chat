import threading
import tkinter as tk
import receiver
import sender

# Create the main window
root = tk.Tk()
root.geometry("400x500")

# Create an entry box to connect to an IP
ip_field = tk.Entry(root, width=50)
ip_field.pack(pady=10)

# Button to connect to an IP
connect_button = tk.Button(root, text="Connect", width=10)
connect_button.pack()

# Textbox to display messages
messages = tk.Text(root, state="disabled", height=20, width=50)
messages.pack(pady=10)

# Function to write content into textbox
def EnterMessage(message):
    messages.configure(state="normal")
    messages.insert("end", message + "\n")
    messages.configure(state="disabled")
    entry.delete(0, "end")

# Entry box to type messages
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Button to send messages
send_button = tk.Button(root, text="Send", width=10)
send_button.pack()

# Functionality
send = sender.Sender(EnterMessage)

ip_field.bind("<Return>", (lambda event: send.Start(ip_field.get())))
connect_button.configure(command=lambda: send.Start(ip_field.get()))

entry.bind("<Return>", (lambda event: send.SendMessage(entry.get())))
send_button.configure(command=lambda: send.SendMessage(entry.get()))

receive = receiver.Receiver(EnterMessage)
receiverThread = threading.Thread(target=receive.Start, daemon=True)
receiverThread.start()

# Run the app
root.mainloop()