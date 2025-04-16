import random
import string

# Creates a random password for the user to use.
class RegeneratePassword:
    def __init__(self):
        self.password_length = 20 # You can change the default length here

    def generate(self):
        """Generates a random password with letters and digits."""
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=self.password_length))
        return password

    def execute(self , user_input=None):
        """Executes the password regeneration and returns the new password."""
        new_password = self.generate()
        return f"Your new password is: {new_password}"
