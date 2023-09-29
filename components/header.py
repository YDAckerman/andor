from src.nest_message.nested_bitmap import NestedBitmap

UNITS = 'em'
PAD = [1, 0]
BITS = 16
R = 1.2 / BITS
HEIGHT = R * BITS
RIGHT_MSG = '&more'
LEFT_MSG = 'a/o'

FRONT_COLOR, LINK_COLOR = ['Red', 'Blue']

FRONT_BITMAPS = [NestedBitmap(msg, BITS, PAD, UNITS, FRONT_COLOR)
                 for msg in [LEFT_MSG, RIGHT_MSG]]

LINK_BITMAPS = [NestedBitmap(msg, BITS, PAD, UNITS, LINK_COLOR)
                for msg in [LEFT_MSG, RIGHT_MSG]]

HEADER = {
    'left': {
        'path': 'andor',
        'front_styles': FRONT_BITMAPS[0].get_css_styles(R),
        'link_styles': LINK_BITMAPS[0].get_css_styles(R),
        'width': R * len(LEFT_MSG) * BITS
    },
    'right': {
        'path': 'more',
        'front_styles': FRONT_BITMAPS[1].get_css_styles(R),
        'link_styles': LINK_BITMAPS[1].get_css_styles(R),
        'width': R * len(RIGHT_MSG) * BITS
    },
    'height': HEIGHT,
    'units': UNITS
}
