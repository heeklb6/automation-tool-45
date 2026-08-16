import json
import re
from validators import validate_input

class CryptoAutomation:
    def __init__(self):
        self.data = []

    def main_loop(self):
        while True:
            user_input = input('Enter command: ')
            if validate_input(user_input):
                self.process_command(user_input)
            else:
                print('Invalid input, please try again.')

    def process_command(self, command):
        # Simulating command processing
        print(f'Processing command: {command}')

if __name__ == '__main__':
    automation = CryptoAutomation()
    automation.main_loop()
