# say you have the boring task of finding every phone number and email address in a long web page
# or document. Look at the full picture we need to do the following:
# 1. Get the text off clipboard
# 2. Find all phone numbers and email addresses in the text.
# 3. Paste them onto the clipboard.

# We can use `pyperclip` module for step 1 and 3 and `re` module for step 2. Like this:
# 1. Use the `pyperclip` to copy and paste strings.
# 2. Create two regexes, one for matching phone numbers and the other for matching email addresses.
# 3. Find all matches, not just the first match, of both regexes.
# 4. Neatly format the matched strings into a single string to paste.
# 5. Display some kind of message if no matches were found in the text.

#! python3
# phone_number_email_address.py - Finds phone numbers and email addresses on the clipboard.


import re
import pyperclip

# Create regex for phone-number
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    \.[a-zA-Z]{2,4}     # dot extension
''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []

# Extract phone numbers
matches = []
for groups in phoneRegex.findall(text):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum
                      )
# Extract email addresses
for groups in emailRegex.findall(text):
    matches.append(groups)

# Copy results to the clipboard
if matches:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')



