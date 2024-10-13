import re
import pyperclip


def clean_typos(text):
    # Remove multiple spaces
    text = re.sub(r'\s{2,}', ' ', text)  # Replace multiple spaces with a single space

    # Remove repeated words
    text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text)  # Replace repeated words with a single instance

    # Remove multiple exclamation marks
    text = re.sub(r'!{2,}', '!', text)  # Replace multiple exclamation marks with a single one

    return text


# Get text from clipboard
text = pyperclip.paste()

# Clean the text
cleaned_text = clean_typos(text)

# Output the cleaned text
print(cleaned_text)

# Optionally copy cleaned text back to clipboard
pyperclip.copy(cleaned_text)
