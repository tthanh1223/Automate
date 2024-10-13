#p! python3
# findURL.py - find website URLs that begin with http:// or https://

import re
import pyperclip

text = pyperclip.paste()

urlJustHttpRegex = re.compile(r'https?:\/\/\S+[^\s.,!?)\]]')
matches = urlJustHttpRegex.finditer(text)

for match in matches:
    print(match.group())