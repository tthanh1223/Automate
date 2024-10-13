# sensitiveInfor.py - Remove sensitive information such as
# Social Security or credit card numbers.

import pyperclip
import re

text = pyperclip.paste()

def remove_sensitive_info(text):
    # Regex patterns for SSN and credit card numbers
    ssnRegex = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
    creditRegex = re.compile(r'\b(?:\d{4}[- ]?){3}\d{4}\b|\b(\d{4})[- ](\d{,7})[- ](\d{,5})\b')
    text = ssnRegex.sub('[REDACTED SSN]', text)
    text = creditRegex.sub('[REDACTED CREDIT]', text)
    return text
cleaned_text = remove_sensitive_info(text)
print(cleaned_text)
pyperclip.copy(cleaned_text)