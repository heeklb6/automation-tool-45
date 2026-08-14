import json

class InputValidationError(Exception):
    pass

class CryptoHandler:
    def __init__(self):
        self.allowed_commands = {'buy', 'sell', 'balance'}

    def validate_input(self, command):
        if command not in self.allowed_commands:
            raise InputValidationError(f"Invalid command: {command}")

    def process_command(self, command):
        try:
            self.validate_input(command)
            # Process the command
            return f"Processing command: {command}"
        except InputValidationError as e:
            return str(e)

    def main_loop(self):
        while True:
            user_input = input("Enter command: ").strip()
            response = self.process_command(user_input)
            print(response)

if __name__ == '__main__':
    handler = CryptoHandler()
    handler.main_loop()