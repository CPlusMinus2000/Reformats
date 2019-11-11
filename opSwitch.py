import pyperclip as pyp

lines = list(pyp.paste().split('\n'))
toPaste = ""

for line in lines:
    if "&plus" in line:
        toPaste += line.replace("&plus", "&minus")
    elif "+" in line:
        toPaste += line.replace("+","-")
    elif "&minus" in line:
        toPaste += line.replace("&minus","&plus")
    elif "−" in line:
        toPaste += line.replace("−","+")
    else:
        toPaste += line

pyp.copy(toPaste)