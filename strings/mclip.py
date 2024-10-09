#! python3
# mclip.py A multi-clipboard program.
"""
If you’ve responded to a large number of emails with similar phrasing, you’ve probably had to do a lot of repetitive typing. 
Maybe you keep a text document with these phrases so you can easily copy and paste them using the clipboard. 
But your clipboard can only store one message at a time, which isn’t very convenient. 
Let’s make this process a bit easier with a program that stores multiple phrases."""

TEXT = {'argee':"""Yes, I agree. That sounds great to me.""",
        'consider':""" I really want to join with you but I have some problems. I call later.""",
        'busy':"""Sorry, but I'm busy this week. Can we delay for the next one?""",
        'upsell':"""Would you consider making this a monthly donation?"""}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit(1)

keyphrase = sys.argv[1] #first command-line argument is the keyphrase.
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
else:
    print('There is no text for' + keyphrase)
