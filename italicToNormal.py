import pyperclip as pyp

modes = [1, 2, 5, 7] # Which modes are active?
lines = list(pyp.paste().split("\n"))
ignore = [chr(c) for c in range(ord('A'), ord('z') + 1)]
ignore += ["xh","kx","kh","ah","&prime;"]
trig = ["sin","cos","tan","csc","sec","cot","$func","func1","$func2"]
signs = ["$sign","$sign1","$sign2","$sign3","$sign4"]

toPaste = ""
for line in lines:

    # Erasing incompleteness styling
    if 1 in modes and "mstyle" in line:
        continue

    # Getting rid of excess space
    if 2 in modes and ("<mo>&nbsp;</mo>" in line or "mspace" in line):
        continue

    # Making italicized words normal (except those in ignore)
    if 3 in modes:
        if '"italic">' in line:
            start = line.find('"italic">') + len('"italic>"')
            end = line.find('</mi>')
            if line[start:end] not in ignore:
                toPaste += line.replace("italic", "normal")
                continue
    
    # Turning numbers bold
    if 4 in modes:
        if "<mn>" in line:
            toPaste += line.replace("<mn>", '<mn mathvariant="bold">')
            continue
    
    # Changing trig operations to have the mo (math operator) tag
    if 5 in modes:
        if any(['>' + func + '<' in line for func in trig]) and "mi>" in line:
            toPaste += line.replace("mi>", "mo>")
            continue
        elif any(['>' + func + '<' in line for func in trig]) and "mn>" in line:
            toPaste += line.replace("mn>", "mo>")
            continue
    
    # Changing commas to be numbers rather than operators (for thousands)
    if 6 in modes:
        if "<mo>&comma;</mo>" in line:
            toPaste += line.replace("mo","mn")
            continue
    
    # For algorithmic variables, changing from mn to mo
    if 7 in modes:
        if any(['>' + op + '<' in line for op in signs]) and "mn>" in line:
            toPaste += line.replace("mn>","mo>")
            continue

    toPaste += line
            
pyp.copy(toPaste)
