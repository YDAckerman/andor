from src.nest_message.nested_bitmap import NestedBitmap

UNITS = 'em'
PAD = [1, 0]
BITS = 8
R = 1.5 / BITS
MSG_COLOR = "Purple"
BEEP_COLOR = "Yellow"
MSG_LINES = [
    "hi!                   ",
    "                      ",
    "you've reached yoni.  ",
    "i'm away from my      ",
    "website right now.    ",
    "please leave a message",
    "after the...          ",
    "                      ",
    "                      ",
    "*BEEP*"
]

BEEP_BITMAP = NestedBitmap(MSG_LINES[-1], BITS, PAD, UNITS, BEEP_COLOR)
BEEP_BITMAP.replace_bits('█')

MSG_BITMAP = NestedBitmap(MSG_LINES[0], BITS, PAD, UNITS, MSG_COLOR)
for line in MSG_LINES[1:-1]:
    MSG_BITMAP.append(
        NestedBitmap(line, BITS, PAD, UNITS, MSG_COLOR)
    )

MESSAGE = {
    'message': {
        'text': MSG_BITMAP.get_html_text(),
        'styles': MSG_BITMAP.get_css_styles(R),
        'width': R * len(MSG_LINES[0]) * BITS
    },
    'beep': {
        'text': BEEP_BITMAP.get_html_text(),
        'styles': BEEP_BITMAP.get_css_styles(R),
        'width': R * len(MSG_LINES[0]) * BITS
    },
    'height': R * len(MSG_LINES) * BITS,
    'units': UNITS
}
