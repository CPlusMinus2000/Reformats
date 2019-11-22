import pyperclip as pyp

lines = pyp.paste()
toPaste = ""
ops = ['+','-','/','=']

for i in range(len(lines)):

    if lines[i] in ops and lines[i - 1] != ' ':
        toPaste += ' '
    
    toPaste += lines[i]

    if lines[i] in ops and lines[i + 1] != ' ':
        toPaste += ' '

pyp.copy(toPaste)
