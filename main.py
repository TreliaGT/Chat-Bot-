
from dotenv import load_dotenv
import os

load_dotenv() 

from ui.chatbot_ui import ChatBotWindow
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotWindow(root)
    root.mainloop()
