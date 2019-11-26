# Script for surrounding variables in mathML tags
import pyperclip as pyp

ignore = ["$word" + c for c in [''] + [str(n) for n in range(1,5)]]
ignore += ["$place", "$an"]
mStart = '<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow> <mn>'
mEnd = '</mn> </mrow></math> '

def main() -> None:
    toPaste = ""
    for word in pyp.paste().split(' '):
        if '$' in word and word not in ignore:
            toPaste += mStart + word + mEnd
        else:
            toPaste += word + ' '
    
    pyp.copy(toPaste[:-1]) # Get rid of the last space

if __name__ == "__main__":
    main()
