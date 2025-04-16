# Desktop Buddy ChatBot

**Desktop Buddy** is a fun, interactive chatbot created with Python using **customtkinter** for a desktop application interface and **chatbot.py** to handle the logic of natural language processing and interaction. The bot is capable of responding to various user inputs, providing jokes, time, weather information, performing math calculations, and more.

## Features

- **Interactive Chat Interface**: The chatbot has a clean, user-friendly chat window built using customtkinter.
- **Customizable Responses**: The bot can respond to different triggers based on a configurable JSON file.
- **Basic Chatbot Functions**:
  - **Tell Jokes**
  - **Tell Time**
  - **Get Weather**
  - **Math Solutions**
  - Custom responses to user queries
- **Grabbing Data from JSON**: Responses are loaded from a JSON file, allowing easy modification or expansion of chatbot capabilities.
  
## Technologies Used

- **Python**: Main programming language.
- **customtkinter**: Custom Tkinter-based GUI framework for the chat interface.
- **PIL (Python Imaging Library)**: Used for handling bot icon images.
- **JSON**: For storing and retrieving response triggers and actions.
- **requests**: For making HTTP requests (e.g., for getting weather data).
- **sympy**: For performing symbolic mathematics (e.g., solving math problems).


## Installation

To run the chatbot, you'll need to have Python installed on your computer.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/desktop-buddy-chatbot.git
   cd desktop-buddy-chatbot```

2. **Install dependencies**:
     You can use pip to install all the required packages listed in the requirements.txt file:
     ```pip install -r requirements.txt ```

3. **Run the application**:
    After installing the required packages, you can run the chatbot application by executing the following:
    ```python main.py ```

