# Script that rearranges figures, formatting them to be in the desired format
import pyperclip as pyp

template = ('<figure>'
            '<img alt="ALTTEXT" class="center" data-media-type="image/jpg"'
            ' src="LINK" /><figcaption><span class="OpenStaxChem-fig-label">'
            'Figure NUMBER</span>CAPTION</figcaption></figure>')

# Finds all substrings in the given superstring and returns their indices.
def findAll(superstring: str, substring: str):
    indices = []
    index = superstring.find(substring)
    
    while index != -1: # -1 means that the substring is not present
        indices.append(index)
        index = superstring.find(substring, index + 1)
    
    return indices

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
def main() -> None:
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
    main()
