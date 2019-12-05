# Code that finds and inserts tooltip definitions
import pyperclip as pyp

# Make a big long string that contains the format of tooltips.
formatted = '<span class="OpenStaxChem-term">TERM'
formatted += '<span class="OpenStaxChem-definition">'
formatted += '<span class="OpenStaxChem-t">TERM</span>DEFINITION</span></span>'

template = ('<figure>'
            '<img alt="ALTTEXT" class="center" data-media-type="image/jpg"'
            ' src="LINK" /><figcaption><span class="OpenStaxChem-fig-label">'
            'Figure NUMBER</span>CAPTION</figcaption></figure>')

# Path of manifest and any pieces of text that should go into MathML
source = "../../OpenStax Backups/Chemistry/manifest.xml"
mathify = ["&#960;", "&#963;"]

# Find all substrings, which is useful for pinpointing the locations of all
#  of the terms which need definitions.
def findAll(superstring: str, substring: str):
    ret = []
    index = superstring.find(substring)
    
    while (index != -1): # -1 means that the substring is not present
        ret.append(index)
        index = superstring.find(substring, index + 1)
    
    return ret

# Converting strings to MathML, specifically numbers and certain letters.
def mathMLulate(text: str, mType: str="let") -> str:
    sTags = { # Dictionary of all starting tags
        "let": '<mi mathvariant="italic">',
        "num": '<mn>',
        "ign": '<mi mathvariant="normal">'
    }
    eTags = { # Dictionary of all ending tags
        "let": '</mi>',
        "num": '</mn>',
        "ign": '</mi>'
    }

    start = '<math xmlns="http://www.w3.org/1998/Math/MathML">\n<mrow>\n'
    start += sTags[mType]
    end = eTags[mType] + '\n</mrow>\n</math>'

    return start + text + end

# Given a keyword, this function finds the corresponding definition and formats
#  it into a tooltip, returning said tooltip as a string.
def makeTooltip(text: str) -> str:
    filled = formatted.replace("TERM", text, 1)
    definition = "DEFINITION NOT FOUND" # The default value

    with open(source, 'r', encoding="utf-8") as manifest:
        data = manifest.read() # Get the manifest data as a string.
        toFind = "<dt>" + text.lower() + "</dt>"
        defIndex = data.find(toFind)

        if defIndex != -1: # Actually found it, so replace out the term
            filled = filled.replace("TERM", text.lower())

        if defIndex == -1: # Maybe it contains a proper name? No lowercasing.
            toFind = "<dt>" + text + "</dt>"
            defIndex = data.find(toFind)
            filled = filled.replace("TERM", text)

        if defIndex == -1: # Maybe it's a plural? Try removing the s and check.
            toFind = "<dt>" + text[:-1].lower() + "</dt>"
            defIndex = data.find(toFind)
            filled = filled.replace("TERM", text[:-1].lower())
        
        if defIndex == -1: # Maybe it's a plural with a proper name?
            toFind = "<dt>" + text[:-1] + "</dt>"
            defIndex = data.find(toFind)
            filled = filled.replace("TERM", text[:-1])
        
        if defIndex == -1: # Still can't find it? Report it.
            filled = filled.replace("TERM", text.lower())
            return filled.replace("DEFINITION", definition)
        
        defIndex += len(toFind) + 2 # Add a bit of extra length
        definition = data[data.find('>', defIndex) + 1:data.find('<', defIndex)]

        # Here are a couple loops just to check for MathML-ing things
        for repl in mathify:
            if repl in definition:
                definition = definition.replace(repl, mathMLulate(repl, "let"))
        
        for word in definition.split():
            if word.isdigit():
                definition = definition.replace(word, mathMLulate(word, "num"))
        
    return filled.replace("DEFINITION", definition)

# Combs the text in the clipboard for keywords, making them into tooltips.
def addTooltips() -> None:
    txt = pyp.paste()

    # Make four arrays for outer and inner start and end indices of keywords.
    outSIndices = findAll(txt, '<span data-type="term">')
    inEIndices = [txt.find('</span>', s) for s in outSIndices]
    inSIndices = [i + len('<span data-type="term">') for i in outSIndices]
    outEIndices = [i + len('</span>') for i in inEIndices]
    
    # Replace all of the keywords with their corresponding tooltips, making
    #  sure to move backwards so as not to mess up other indices.
    for i in reversed(range(len(inEIndices))):
        inner = txt[inSIndices[i]:inEIndices[i]]
        outer = txt[outSIndices[i]:outEIndices[i]]
        txt = txt.replace(outer, makeTooltip(inner), 1)
    
    # Copy the formatted text.
    pyp.copy(txt)

# Makes a new, properly formatted figure given the old figure passed in as text.
#  Note: the abundance of +1's and -2's in this function is due to the fact
#  that quotation marks will be present in both the old figure and the template
#  figure, so I need to get rid of them from the old figure using +1/-2's.
def makeFigure(text: str) -> str:
    # Get the caption
    capStart = text.find("</span>") + len("</span>")
    caption = text[capStart:text.find("</figcaption>")]
    
    # Get the alt text
    altLoc = text.find("img alt=") + len("img alt=") + 1
    altEnd = text.find("data-media-type=") - 2 # Slice off the last quotation
    altText = text[altLoc:altEnd]

    # Get the image link
    linkLoc = text.find("src=") + len("src=") + 1
    linkEnd = text.find("/>", linkLoc) - 2
    link = text[linkLoc:linkEnd]

    # Construct the new figure and return
    figure = template.replace("ALTTEXT", altText)
    figure = figure.replace("LINK", link)
    return figure.replace("CAPTION", caption)

# Parses the clipboard text for all old figures, and passes them incrementally
#  back into the clipboard for pasting.
def addFigures() -> None:
    txt = pyp.paste()

    # Make four arrays for outer and inner start and end indices of keywords.
    sIndices = findAll(txt, '<figure')
    eIndices = [txt.find('</figure>', i) + len('</figure>') for i in sIndices]
    
    # Replace all of the keywords with their corresponding tooltips, making
    #  sure to move backwards so as not to mess up other indices.
    for i in reversed(range(len(sIndices))):
        oldFigure = txt[sIndices[i]:eIndices[i]]
        txt = txt.replace(oldFigure, makeFigure(oldFigure), 1)
    
    # Copy the formatted text.
    pyp.copy(txt)

if __name__ == "__main__":
    addTooltips()
    addTooltips()
