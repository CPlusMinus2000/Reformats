# Short script that adds extra information to existing tags
import pyperclip as pyp

mode = 1

# List of Modes:
#  1. Displaying text above/below summations
#  2. Adding bold text to mi/mn tags

tags = {
    1: 'displaystyle="true" movablelimits="false"',
    2: 'mathvariant="bold"'
}

tagEnd = pyp.paste().find('>')
toPaste = pyp.paste()[:tagEnd] + ' ' + tags[mode] + pyp.paste()[tagEnd:]

pyp.copy(toPaste)