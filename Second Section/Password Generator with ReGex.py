# Password Generator with ReGex
# User specified Password Length and constraints (maximum number of each type of character)
# Uses secrets module for cryptographic security (instead fo random module)

import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),   # \W doesn't consider _ as a special character
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        # generator instead of list comprehension
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break    # exit while, successful password built
    
    return password


if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)