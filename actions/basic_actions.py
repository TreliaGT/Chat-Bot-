import requests
import json
import os

#tells Joke
class TellJoke():
    def pull_joke(self):
        response = requests.get(os.getenv('JOKE_API'))
        data = response.json()
        return data

    def execute(self):
        setup	= self.pull_joke()["setup"]
        punchline	= self.pull_joke()["punchline"]
        return f"{setup} \n {punchline}"