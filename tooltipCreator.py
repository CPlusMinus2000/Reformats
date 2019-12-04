# Code that finds and inserts tooltip definitions
import pyperclip as pyp

formatted = '<span class="OpenStaxChem-term">TERM'
formatted += '<span class="OpenStaxChem-definition">'
formatted += '<span class="OpenStaxChem-t">TERM</span>DEFINITION</span></span>'
source = "../../OpenStax Backups/Chemistry/manifest.xml"
mathify = ["&#960;", "&#963;"]

def findAll(superstring: str, substring: str):
    ret = []
    index = superstring.find(substring)
    
    while (index != -1): # -1 means that the substring is not present
        ret.append(index)
        index = superstring.find(substring, index + 1)
    
    return ret

def mathMLulate(text: str, mType: str="let") -> str:
    sTags = {
        "let": '<mi mathvariant="italic">',
        "num": '<mn>',
        "ign": '<mi mathvariant="normal">'
    }
    eTags = {
        "let": '</mi>',
        "num": '</mn>',
        "ign": '</mi>'
    }

    start = '<math xmlns="http://www.w3.org/1998/Math/MathML">\n<mrow>\n'
    start += sTags[mType]
    end = eTags[mType] + '\n</mrow>\n</math>'

    return start + text + end

def makeTooltip(text: str) -> str:
    filled = formatted.replace("TERM", text, 1).replace("TERM", text.lower())
    definition = ""

    with open(source, 'r', encoding="utf-8") as manifest:
        data = manifest.read()
        toFind = "<dt>" + text.lower() + "</dt>"
        defIndex = data.find(toFind)

        if defIndex == -1:
            toFind = "<dt>" + text[:-1].lower() + "</dt>"
            defIndex = data.find(toFind)
        
        if defIndex == -1:
            return filled.replace("DEFINITION", "DEFINITION NOT FOUND")
        
        defIndex += len(toFind) + 2
        definition = data[data.find('>', defIndex) + 1:data.find('<', defIndex)]

        for repl in mathify:
            if repl in definition:
                definition = definition.replace(repl, mathMLulate(repl, "let"))
        
        for word in definition.split():
            if word.isdigit():
                definition = definition.replace(word, mathMLulate(word, "num"))
        
    return filled.replace("DEFINITION", definition)

def main() -> None:
    txt = pyp.paste()

    outSIndices = findAll(txt, '<span data-type="term">')
    inEIndices = [txt.find('</span>', s) for s in outSIndices]
    inSIndices = [i + len('<span data-type="term">') for i in outSIndices]
    outEIndices = [i + len('</span>') for i in inEIndices]
    
    for i in reversed(range(len(inEIndices))):
        inner = txt[inSIndices[i]:inEIndices[i]]
        outer = txt[outSIndices[i]:outEIndices[i]]
        txt = txt.replace(outer, makeTooltip(inner), 1)
    
    pyp.copy(txt)

if __name__ == "__main__":
    main()
