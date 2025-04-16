import tkinter as tk
from tkinter import scrolledtext
from chatbot.chatbot import ChatBot  # Adjust if chatbot.py is in chatbot/ folder


class ChatBotWindow:
    def __init__(self, root):
        self.bot = ChatBot()
        self.bot.greet()  # You can show this message in the chat window
        self.root = root

        root.title("Desktop Buddy 🤖")
        root.geometry("400x500")
        root.resizable(False, False)

        self.chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Segoe UI", 10))
        self.chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry_field = tk.Entry(root, font=("Segoe UI", 10))
        self.entry_field.pack(padx=10, pady=(0,10), fill=tk.X)
        self.entry_field.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=(0, 10))

        self.add_bot_message(f"Hello! I'm {self.bot.name}. Type 'bye' to exit.")

    def add_bot_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, f"{self.bot.name}: {message}\n")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

    def add_user_message(self, message):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, f"You: {message}\n")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

    def send_message(self ,event=None):
        user_input = self.entry_field.get().strip()
        if not user_input:
            return
        self.add_user_message(user_input)
        self.entry_field.delete(0, tk.END)

        response = self.bot.get_response(user_input)
        self.add_bot_message(response)

        if not self.bot.running:
            self.root.after(1500, self.root.destroy) # Close window after bye

