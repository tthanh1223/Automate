#Pig Latin is a silly made-up language that alters English words.
# If a word begins with a vowel, the word yay is added to the end of it.
# If a word begins with a consonant or consonant cluster (like ch or gr),
# that consonant or cluster is moved to the end of the word followed by ay.

#Let’s write a Pig Latin program that will output something like this:
"""
Enter the English message to translate into Pig Latin:
<plain>
<plain with pig latin style>
"""
import sys
def translate_pig_latin(trans_text:list[str]):
    vowels = ('a', 'e', 'i', 'o', 'u','y')
    pig_latins = []

    for word in trans_text:
        #Separate non-letter at first
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            pig_latins.append(prefix_non_letters)
            continue

        #Separate non-letter at end
        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]

        # Uppercase or title
        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower() # make it lowercase for translation.

        # Separate the consonants at the start of this word:
        prefix_consonants = ''
        while len(word) > 0 and not word[0] in vowels:
            prefix_consonants += word[0]
            word = word[1:]

        # Add pig Latin
        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        if was_upper:
            word = word.upper()
        elif was_title:
            word = word.title()

        pig_latins.append(prefix_non_letters+word+suffix_non_letters)
    print(' '.join(pig_latins))

if __name__ == '__main__':
    text = sys.stdin.read()
    lines = text.split('\n')
    words = []
    for line in lines:
        words.extend(line.split())
    print("Enter the English message to translate into Pig Latin:")
    print(text,end='')
    translate_pig_latin(words)