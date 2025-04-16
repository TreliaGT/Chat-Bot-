import requests
import json
import os
from datetime import datetime


#tells Joke
class TellJoke():
    def pull_joke(self):
        response = requests.get(os.getenv('JOKE_API'))
        data = response.json()
        return data

    def execute(self , user_input=None):
        setup	= self.pull_joke()["setup"]
        punchline	= self.pull_joke()["punchline"]
        return f"{setup} \n {punchline}"

class TellTime:
    def execute(self , user_input=None):
        now = datetime.now()
        return now.strftime("The current time is %H:%M:%S")