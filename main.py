
from dotenv import load_dotenv
import os

load_dotenv() 

from ui.chatbot_ui import ChatBotWindow
import customtkinter as ctk

if __name__ == "__main__":
    root = ctk.CTk()  # Create the main window
    app = ChatBotWindow(root)  # Initialize the chatbot window
    root.mainloop()  # Start the GUI loop
