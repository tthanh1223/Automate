# Create a Mad Libs program that reads in text files and lets the user add their own text anywhere
#   the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
#   For example, a text file may look like this:
#       The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
#       unaffected by these events.
# The program would find these occurrences and prompt the user to replace them.
    # Enter an adjective:
    #   silly
    # Enter a noun:
    #   chandelier
    # Enter a verb:
    #   screamed
    # Enter a noun:
    #   pickup truck

# The following text file would then be created:
    # The silly panda walked to the chandelier and then screamed. A nearby pickup
    # truck was unaffected by these events.
# The results should be printed to the screen and saved to a new text file.

#! python3
placeholders = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB']
with open('text.txt','r') as textFile:
    content = textFile.read()
for placeholder in placeholders:
    while placeholder in content:
        user_input = input(f'Enter a {placeholder.lower()}: ')
        content = content.replace(placeholder,user_input, 1)

print("\nHere is your Mad Libs story:\n")
print(content)
with open('madlib_result.txt','w') as resultFile:
    resultFile.write(content)
print("\nThe result has been saved to 'madlib_result.txt'")
