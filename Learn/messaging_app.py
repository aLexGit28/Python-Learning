import tkinter as tk
from collections import defaultdict, deque


class MessagingAppGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Messaging Application")
        self.master.geometry("800x700")
        self.master.configure(bg="#C4E4FF")

        self.message_queue = defaultdict(deque)

        # Sender
        self.sender_label = tk.Label(master, text="Sender:", bg="#C4E4FF")
        self.sender_label.grid(row=0, column=0, padx=10, pady=5)

        self.sender_entry = tk.Entry(master)
        self.sender_entry.grid(row=0, column=1, padx=10, pady=5)

        # Receiver
        self.receiver_label = tk.Label(master, text="Receiver:", bg="#C4E4FF")
        self.receiver_label.grid(row=1, column=0, padx=10, pady=5)

        self.receiver_entry = tk.Entry(master)
        self.receiver_entry.grid(row=1, column=1, padx=10, pady=5)

        # Message
        self.message_label = tk.Label(
            master, text="Message:", bg="#C4E4FF"
        )
        self.message_label.grid(row=2, column=0, padx=10, pady=5)

        self.message_entry = tk.Entry(master)
        self.message_entry.grid(row=2, column=1, padx=10, pady=5)

        # Send button
        self.send_button = tk.Button(
            master,
            text="Send Message",
            command=self.send_message
        )
        self.send_button.grid(
            row=3, columnspan=2, padx=10, pady=5
        )

        # Receiver to receive messages
        self.receive_label = tk.Label(
            master, text="Receiver:", bg="#C4E4FF"
        )
        self.receive_label.grid(
            row=4, column=0, padx=10, pady=5
        )

        self.receiver_to_receive_entry = tk.Entry(master)
        self.receiver_to_receive_entry.grid(
            row=4, column=1, padx=10, pady=5
        )

        # Receive button
        self.receive_button = tk.Button(
            master,
            text="Receive Messages",
            command=self.receive_messages
        )
        self.receive_button.grid(
            row=5, columnspan=2, padx=10, pady=5
        )

        # Sent messages
        self.sent_messages_label = tk.Label(
            master,
            text="Sent Messages:",
            bg="#C4E4FF"
        )
        self.sent_messages_label.grid(row=6, column=0, padx=10, pady=5)

        self.sent_messages_text = tk.Text(
            master, height=5, width=30
        )
        self.sent_messages_text.grid(
            row=6, column=1, padx=10, pady=5
        )

        # Received messages
        self.received_messages_label = tk.Label(
            master,
            text="Received Messages:",
            bg="#C4E4FF"
        )
        self.received_messages_label.grid(
            row=7, column=0, padx=10, pady=5
        )

        self.received_messages_text = tk.Text(
            master, height=5, width=30
        )
        self.received_messages_text.grid(
            row=7, column=1, padx=10, pady=5
        )

    def send_message(self):
        sender = self.sender_entry.get()
        receiver = self.receiver_entry.get()
        message = self.message_entry.get()

        if sender != "" and receiver != "" and message != "":
            self.message_queue[receiver].append(
                (sender, message)
            )

            self.sent_messages_text.insert(
                tk.END,
                f"Sent to {receiver}: {message}\n"
            )

            self.message_entry.delete(0, tk.END)

    def receive_messages(self):
        receiver = self.receiver_to_receive_entry.get()

        self.received_messages_text.delete(
            "1.0", tk.END
        )

        if receiver in self.message_queue:

            self.received_messages_text.insert(
                tk.END,
                f"Messages for {receiver}:\n"
            )

            while self.message_queue[receiver]:

                sender, message = (
                    self.message_queue[receiver].popleft()
                )

                self.received_messages_text.insert(
                    tk.END,
                    f"From {sender}: {message}\n"
                )

        else:
            self.received_messages_text.insert(
                tk.END,
                f"No messages for {receiver}\n"
            )

        self.receiver_to_receive_entry.delete(
            0, tk.END
        )


root = tk.Tk()

app = MessagingAppGUI(root)

root.mainloop()