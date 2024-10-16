# Let’s rewrite the “multi-clipboard” program from Chapter 6 so that it uses the `shelve` module.
# The user will now be able to save new strings to load to the clipboard without having to modify the source code.
# We’ll name this new program mcb.pyw (since “mcb” is shorter to type than “multi-clipboard”).
# The .pyw extension means that Python won’t show a Terminal window when it runs this program. (See Appendix B for more details.)
# The program will save each piece of clipboard text under a keyword.
# For example, when you run py mcb.pyw save spam,
#   the current contents of the clipboard will be saved with the keyword spam.
#   This text can later be loaded to the clipboard again by running py mcb.pyw spam.
#   And if the user forgets what keywords they have,
#       they can run py mcb.pyw list to copy a list of all keywords to the clipboard.

# Here’s what the program does:
#   The command line argument for the keyword is checked.
#   If the argument is _save_, then the clipboard contents are saved to the keyword.
#   If the argument is _list_, then all the keywords are copied to the clipboard.
#   Otherwise, the text for the keyword is copied to the clipboard.
# This means the code will need to do the following:
#   Read the command line arguments from sys.argv.
#   Read and write to the clipboard.
#   Save and load to a shelf file.
# If you use Windows, you can easily run this script from the Run...
#   window by creating a batch file named mcb.bat with the following content:
# @pyw.exe C:\Python34\mcb.pyw %*

#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
# List keywords and load content.
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        for key in mcbShelf:
            del mcbShelf[key]
mcbShelf.close()