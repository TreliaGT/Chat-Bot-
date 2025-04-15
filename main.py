import json
import re
from dotenv import load_dotenv
import os

load_dotenv() 

from actions.regenerate_password import RegeneratePassword
from actions.basic_actions import TellJoke
from actions.get_weather import GetWeather

# Reads json input.
class JsonHandler:
    def __init__(self, trigger_key, triggers, response, action=None):
        self.trigger_key = trigger_key
        self.triggers = triggers
        self.response = response
        self.action = action  # Store the action (class or function)

    def can_handle(self, user_input):
        return any(re.fullmatch(trigger, user_input) for trigger in self.triggers)

    def handle(self, user_input):
        # If an action is assigned and it's a class, instantiate and call the method
        if self.action:
            action_instance = self.action()  # Create an instance of the action class
            return action_instance.execute()  # Call the execute method
        return self.response


#default handler.
class DefaultHandler:
    def can_handle(self, user_input):
        return True  # Always matches if nothing else did

    def handle(self, user_input):
        return "I'm not sure how to respond to that. Try 'help' for suggestions."

#main chatbot
class ChatBot:
    def __init__(self, name="ChatBot", response_file="responses.json"):
        self.name = name
        self.running = True
        self.handlers = self.load_handlers_from_json(response_file)
        self.last_response = None 

    def load_handlers_from_json(self, file_path):
        handlers = []
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    # Assign actions if needed
                    if "action" in value:
                        # If an action is specified in JSON, pass the class constructor
                        action = globals().get(value["action"])
                        handlers.append(JsonHandler(key, value["triggers"], value["response"], action))
                    else:
                        handlers.append(JsonHandler(key, value["triggers"], value["response"]))
        except FileNotFoundError:
            print(f"{self.name}: Error - Could not find {file_path}.")
        handlers.append(DefaultHandler())  # Always include default fallback
        return handlers

    def greet(self):
        print(f"{self.name}: Hello! I'm {self.name}. Type 'bye' to exit.")

    def get_response(self, user_input):
        user_input = user_input.lower()
        if user_input == 'bye':
            self.running = False
            return "Goodbye!"
        for handler in self.handlers:
            if handler.can_handle(user_input):
                response = handler.handle(user_input)
                self.last_response = response
                return response

    
    def get_last_response(self):
        return self.last_response  # Return the last response

    def chat(self):
        self.greet()
        while self.running:
            user_input = input("You: ")
            if user_input.lower() == "last":
                print(f"{self.name}: Last response was: {self.get_last_response()}")
            else:
                response = self.get_response(user_input)
                print(f"{self.name}: {response}")


if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()
