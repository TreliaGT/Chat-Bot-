import customtkinter as ctk
from chatbot.chatbot import ChatBot  # Adjust if chatbot.py is in chatbot/ folder
from PIL import Image

class ChatBotWindow:
    def __init__(self, root):
        self.bot = ChatBot()
        self.bot.greet()  # You can show this message in the chat window
        self.root = root

        root.title("Desktop Buddy 🤖")
        root.geometry("800x500")
        root.resizable(True, True)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green") 
        ctk.CTkFont(family="Georgia", size=16)
        root.bind('<Return>', self.send_message)  # Regular Enter key
        root.bind('<KP_Enter>', self.send_message)  # Keypad Enter key
        
        # Create the tab view
        self.tabview = ctk.CTkTabview(root)
        self.tabview.pack(padx=10, pady=10, fill=ctk.BOTH, expand=True)

        # Create the first tab (Bot Icon and chat)
        tab1 = self.tabview.add("Chat")
        self.bot_icon = ctk.CTkImage(light_image=Image.open("bot_icon.png"),dark_image=Image.open("bot_icon.png"),size=(150, 150))
        self.bot_icon_label = ctk.CTkLabel(tab1, image=self.bot_icon , text="")
        self.bot_icon_label.pack(pady=10)

        # Create the chat log (text widget) in the first tab
        self.chat_log = ctk.CTkTextbox(tab1, wrap="word", state='disabled', font=("Georgia", 16), height=80)
        self.chat_log.pack(padx=10, pady=10, fill=ctk.BOTH, expand=True)  # Use ctk.BOTH

        # Create the second tab (Chat Log)
        tab2 = self.tabview.add("Log")
        self.log_display = ctk.CTkTextbox(tab2, wrap="word", state='disabled', font=("Georgia", 14), height=300)
        self.log_display.pack(padx=10, pady=10, fill=ctk.BOTH, expand=True)

        # Create a frame outside of the tabview for the entry field and send button
        self.input_frame = ctk.CTkFrame(root)
        self.input_frame.pack(padx=10, pady=(0, 10), fill=ctk.X)  # Position below the tabview

        # Create the entry field for user input
        self.entry_field = ctk.CTkEntry(self.input_frame, font=("Georgia", 16), height=40)
        self.entry_field.pack(side=ctk.LEFT, padx=10, pady=10, fill=ctk.X, expand=True)  # Use ctk.X

        # Create the send button
        self.send_button = ctk.CTkButton(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=ctk.RIGHT, padx=10, pady=10)

        self.add_bot_message(f"Hello! I'm {self.bot.name}. Type 'bye' to exit.")

    #creates bot message
    def add_bot_message(self, message):
        self.chat_log.configure(state='normal')  # Use configure instead of config
        self.chat_log.insert(ctk.END, f"{message}\n")  # Use ctk.END
        self.chat_log.configure(state='disabled')  # Use configure instead of config
        self.chat_log.see(ctk.END)  # Use ctk.END
        self.log_display.configure(state='normal')
        self.log_display.insert(ctk.END, f"{self.bot.name}: {message}\n")
        self.log_display.configure(state='disabled')

    #adds user message to logs
    def add_user_message(self, message):
        self.log_display.configure(state='normal')
        self.log_display.insert(ctk.END, f"You: {message}\n")
        self.log_display.configure(state='disabled')

    #sends message to then work out what the bot's repsonse is.
    def send_message(self, event=None):
        user_input = self.entry_field.get().strip()
        if not user_input:
            return

        self.chat_log.configure(state='normal')
        self.chat_log.delete(1.0, ctk.END)  # Delete all existing content in the chat log
        self.chat_log.configure(state='disabled')

        self.add_user_message(user_input)
        self.entry_field.delete(0, ctk.END)  # Use ctk.END

        response = self.bot.get_response(user_input)
        self.add_bot_message(response)

        if not self.bot.running:
            self.root.after(1500, self.root.destroy)  # Close window after "bye"
