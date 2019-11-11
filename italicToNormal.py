import pyperclip as pyp
import re

modes = [0,1,4,5,6]
lines = list(pyp.paste().split("\n"))
ignore = [chr(c) for c in range(ord('A'), ord('z') + 1)]
ignore += ["xh","kx","kh","ah","&prime;"]
trig = ["sin","cos","tan","csc","sec","cot","$func","func1","$func2"]
signs = ["$sign","$sign1","$sign2","$sign3","$sign4"]

def trigInLine(line):
    inLine = False
    for func in trig:
        inLine = inLine or ('>' + func + '<') in line
    
    return inLine

def signInLine(line):
    inLine = False
    for op in signs:
        inLine = inLine or ('>' + op + '<') in line
    
    return inLine

toPaste = ""
for line in lines:

    if -1 in modes and "mstyle" in line:
        continue

    if 0 in modes and ("<mo>&nbsp;</mo>" in line or "mspace" in line):
        continue

    if 1 in modes:
        if '"italic">' in line:
            start = line.find('"italic">') + len('"italic>"')
            end = line.find('</mi>')
            if line[start:end] not in ignore:
                toPaste += line.replace("italic", "normal")
                continue
        

    if 2 in modes:
        if '"italic">' in line:
            start = line.find('"italic">') + len('"italic>"')
            end = line.find("</mi>")

            subline = line[start:end]
            toPaste += line[:start]

            part1 = subline[0] + "</mi>\n"
            part2 = "\t<mn>" + subline[1] + "</mn>\n"
            part3 = '\t<mi mathvariant="italic">' + subline[2] + "</mi>\n"
            part4 = "\t<mn>" + subline[3] + "</mn>"

            toPaste += (part1 + part2 + part3 + part4)
            continue
    
    if 3 in modes:
        if "<mn>" in line:
            toPaste += line.replace("<mn>", '<mn mathvariant="bold">')
            continue
        elif "<mo>&minus;</mo>" in line:
            toPaste += line.replace("<mo>&minus;</mo>", "<mi>-</mi>")
            continue
    
    if 4 in modes:
        if trigInLine(line) and "mi>" in line:
            toPaste += line.replace("mi>", "mo>")
            continue
        elif trigInLine(line) and "mn>" in line:
            toPaste += line.replace("mn>", "mo>")
            continue
    
    if 5 in modes:
        if "<mo>&comma;</mo>" in line:
            toPaste += line.replace("mo","mn")
            continue
    
    if 6 in modes:
        if signInLine(line) and "mn>" in line:
            toPaste += line.replace("mn>","mo>")
            continue

    toPaste += line
            
pyp.copy(toPaste)
