#! python3
# Writes a function that uses regular expressions to make sure the password string
#   is passed strong. A strong password is defined as one that is at least eight characters long,
#       contains both uppercase and lowercase characters, and has at least one digit.
#           You may need to test the string against multiple regex patterns to validate its strength.

import re


def is_strong_password(password):
    # Check for at least 8 characters
    if len(password) < 8:
        return False

    # Regex patterns
    has_uppercase = re.compile(r'[A-Z]')
    has_lowercase = re.compile(r'[a-z]')
    has_digit = re.compile(r'\d')

    # Validate against the regex patterns
    if (has_uppercase.search(password) and
            has_lowercase.search(password) and
            has_digit.search(password)):
        return True

    return False


# Example usage
passwords = [
    "Password123",  # Strong
    "weakpass",  # Weak
    "Weak1",  # Weak (only 5 chars)
    "StrongPassword",  # Weak (no digit)
    "12345678",  # Weak (no letters)
    "Str0ngPass",  # Strong
]

for pwd in passwords:
    print(f"Password: {pwd}, Strong: {is_strong_password(pwd)}")
