import json
import re
from .actions.regenerate_password import RegeneratePassword
from .actions.basic_actions import TellJoke , TellTime
from .actions.get_weather import GetWeather
from .actions.math_solution import MathSolution

#for sorting and getting the json
class JsonHandler:
    def __init__(self, trigger_key, triggers, response, action=None):
        self.trigger_key = trigger_key
        self.triggers = triggers
        self.response = response
        self.action = action

    def can_handle(self, user_input):
        return any(re.fullmatch(trigger, user_input) for trigger in self.triggers)

    def handle(self, user_input):
        if self.action:
            action_instance = self.action()
            return action_instance.execute(user_input)
        return self.response

#handles if the user input.
class DefaultHandler:
    def can_handle(self, user_input):
        return True

    def handle(self, user_input):
        return "I'm not sure how to respond to that. Try 'help' for suggestions."

#basic chatbot functions
class ChatBot:
    def __init__(self, name="ChatBot", response_file="chatbot/responses.json"):
        self.name = name
        self.running = True
        self.handlers = self.load_handlers_from_json(response_file)
        self.last_response = None

    #loads in the json data
    def load_handlers_from_json(self, file_path):
        handlers = []
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    action = globals().get(value.get("action")) if "action" in value else None
                    handlers.append(JsonHandler(key, value["triggers"], value["response"], action))
        except FileNotFoundError:
            print(f"{self.name}: Error - Could not find {file_path}.")
        handlers.append(DefaultHandler())
        return handlers

    #just a greeting when first opens
    def greet(self):
        return f"Hello! I'm {self.name}. Type 'bye' to exit."

    #gets repsonse from json data
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

    #gets last reponse not currently needed
    def get_last_response(self):
        return self.last_response
