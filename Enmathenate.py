# Script for surrounding variables in mathML tags
import pyperclip as pyp

mStart = '<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>'
mEnd = '</mrow></math>'
norm = '<mi mathvariant="normal">NORMAL</mi>'
ital = '<mi mathvariant="italic">ITALIC</mi>'
oper = '<mo>OPERATOR</mo>'
ignore = []
words = ["&sigma;", "&pi;", 's', 'p']
elements = ['H',"He","Li","Be",'B','C','N','O','F',"Ne","Na","Mg","Al","Se",
            'P','S',"Cl","Ar",'K',"Ca","Sc","Ti",'V',"Cr","Mn","Fe","Cd","Ni",
            "Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr",'Y',"Zr","Nb",
            "Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te",'I',"Xe",
            "Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho",
            "Er","Tm","Yb","Lu","Hf","Ta",'W',"Re","Os","Ir","Pt","Au","Hg",
            "Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa",'U',"Np",
            "Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg",
            "Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]

# Combs through the text in the clipboard character by character, looking
#  for text that needs to be replaced.
def charByChar() -> None:
    text = pyp.paste()
    toPaste = ""
    i = 0

    while i < len(text):
        if text[i].isdigit():
            j = i + 1
            while text[i:j].isdigit():
                j += 1
            
            j -= 1

            if text[i:j] in ignore or text[i-1] == text[j] == '"':
                toPaste += text[i:j]
            else:
                toPaste += mStart + "<mn>" + text[i:j] + "</mn>" + mEnd
            
            i = j

        elif text[i:i+5] == "<math":
            j = text.find("</math>", i) + len("</math>")
            toPaste += text[i:j]
            i = j
        
        elif text[i:i+2] in elements:
            if text[i+2:i+9] == "&ndash;":
                elem1 = norm.replace("NORMAL", text[i:i+2])
                dash = oper.replace("OPERATOR", '-')
                if text[i+9:i+11] in elements:
                    elem2 = norm.replace("NORMAL", text[i+9:i+11])
                    i += 11
                elif text[i+9] in elements:
                    elem2 = norm.replace("NORMAL", text[i+9])
                    i += 10
                else: # This case shouldn't ever happen
                    raise Exception("Second element not found")

                toPaste += mStart + elem1 + dash + elem2 + mEnd

            else:
                toPaste += text[i:i+2]
                i += 2
            
        elif text[i] in elements:
            if text[i+1:i+8] == "&ndash;":
                elem1 = norm.replace("NORMAL", text[i])
                dash = oper.replace("OPERATOR", '-')
                if text[i+8:i+10] in elements:
                    elem2 = norm.replace("NORMAL", text[i+8:i+10])
                    i += 10
                elif text[i+8] in elements:
                    elem2 = norm.replace("NORMAL", text[i+8])
                    i += 9
                else: # This case shouldn't ever happen
                    raise Exception("Second element not found")
                
                toPaste += mStart + elem1 + dash + elem2 + mEnd

            else:
                toPaste += text[i]
                i += 1                

        else:
            toPaste += text[i]
            i += 1

    pyp.copy(toPaste) # Get rid of the last space

# Combs through the text in the clipboard (space-delimited) word-by-word, 
#  looking for words that need to be replaced.
def wordByWord() -> None:
    toPaste = ""

    for word in pyp.paste().split(' '):
        if word in words or word in elements:
            toPaste += mStart + "<mi>" + word + "</mi>" + mEnd + ' '
        else:
            toPaste += word + ' '
    
    pyp.copy(toPaste[:-1]) # The very last character is an extra space.

if __name__ == "__main__":
    charByChar()
    wordByWord()
