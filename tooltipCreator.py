# Code that finds and inserts tooltip definitions
import pyperclip as pyp

formatted = '<span class="OpenStaxChem-term">TERM'
formatted += '<span class="OpenStaxChem-definition">'
formatted += '<span class="OpenStaxChem-t">TERM</span>DEFINITION</span></span>'
source = "../../OpenStax Backups/Chemistry/manifest.xml"
mathify = ["&#960;", "&#963;"]

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

def main(text: str) -> str:
    filled = formatted.replace("TERM", text, 1).replace("TERM", text.lower())
    definition = ""

    with open(source, 'r', encoding="utf-8") as manifest:
        data = manifest.read()
        toFind = "<dt>" + text.lower() + "</dt>"
        defIndex = data.find(toFind) + len(toFind) + 2
        definition = data[data.find('>', defIndex) + 1:data.find('<', defIndex)]

        for repl in mathify:
            if repl in definition:
                definition = definition.replace(repl, mathMLulate(repl, "let"))
        
        for word in definition.split():
            if word.isdigit():
                definition = definition.replace(word, mathMLulate(word, "num"))
        
    return filled.replace("DEFINITION", definition)

if __name__ == "__main__":
    txt = pyp.paste()
    inner = txt[(txt.find('>') + 1):txt.rfind('<')]
    outer = txt[txt.find('<'):(txt.rfind('>') + 1)]
    pyp.copy(txt.replace(outer, main(inner)))
