# Short script that adds markup tags to highlighted text
import pyperclip as pyp

mode = 6

# List of Modes:
#  1: Calculator code span environment
#  2: Math term cancellation
#  3: 70% fontsize for limit notation
#  4: Basic MathML tags (mn)
#  5: Span labels (specifically for OpenStaxChem)
#  6: Font-resizing spans (for Wisconsin S2019)

tD1 = {
    1: '<span class="OpenStaxIS-code">',
    2: '<menclose notation="updiagonalstrike">\n',
    3: '<mstyle fontsize="0.7em">\n',
    4: '<math xmlns="http://www.w3.org/1998/Math/MathML">\n<mrow>\n<mn>\n',
    5: '<span class="OpenStaxChem-label">',
    6: '<span style="font-size:16px;">'
}

tD2 = {
    1: '</span>',
    2: '\n</menclose>',
    3: '\n</mstyle>',
    4: '\n</mn>\n</mrow>\n</math>',
    5: '</span>'
    6: '</span>'
}

pyp.copy(tD1[mode] + pyp.paste() + tD2[mode])
