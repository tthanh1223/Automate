#! python3
# Writes a function that takes a string and does the same thing as the strip() string method.
#   If no other arguments are passed other than the string to strip, then whitespace characters
#       will be removed from the beginning and end of the string. Otherwise, the characters
#           specified in the second argument to the function will be removed from the string.


import re
def custom_strip(input_string, chars=None):
    # If no specific characters are provided, default to whitespace characters
    if chars is None:
        chars = r'\s+'  # regex pattern for whitespace characters
    else:
        # Create a regex pattern for the specified characters
        chars = re.escape(chars)  # Escape special characters
        chars = f'[{chars}]+'  # Create a character class for the regex

    # Use re.sub to remove leading and trailing characters
    stripped_string = re.sub(f'^{chars}|{chars}$', '', input_string)

    return stripped_string


# Example usage
print(custom_strip("   Hello, World!   "))  # Output: "Hello, World!"
print(custom_strip("---Hello, World!---", "-"))  # Output: "Hello, World!"
print(custom_strip("###Hello, World!###", "#"))  # Output: "Hello, World!"
print(custom_strip("   Spaces and # @ !   ", " #@"))  # Output: "Spaces and"

# Testing with characters that have special meanings in regex
print(custom_strip("...Hello, World!...", "."))  # Output: "Hello, World!"
