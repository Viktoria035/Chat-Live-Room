# file for utility functions(e.g., generating unique room codes)
import random
from string import ascii_uppercase
from app import rooms

def generate_unique_code():
    while True:
        code = "".join(random.choices(ascii_uppercase, k=4))
        if code not in rooms:
            return code
