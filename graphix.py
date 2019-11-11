import pyperclip as pyp
import re

endChars = [',', ';']
added = True

graph = pyp.paste()

view = graph.find("view =")
xEnd = graph.find('..', view) + len("..")
fEnd = graph.find('..', xEnd) + len("..")

graphLines = list(pyp.paste().split('\n'))
toPaste = ""

i = 0
while "labels" not in graphLines[i]:
    toPaste += graphLines[i]
    i += 1

line = graphLines[i]
toPaste += line.replace('x', '', 1).replace("f(x)", '', 1)

for gLine in graphLines[(i + 1):]:
    if gLine[-1] not in endChars and added:
        toPaste += gLine + ','
        toPaste += "FILL IN"
    