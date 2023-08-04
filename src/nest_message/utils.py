from bdfparser import Bitmap
from .fonts import FONT_16, FONT_8


def merge_str_lists(*args):
    return [''.join(line) for line in zip(*args)]


def unlist(super_list):
    return [element for sub_list in super_list for element in sub_list]


def make_circular(some_list):
    i = 0
    while True:
        yield some_list[i % len(some_list)]
        i += 1


def zero_out(bitmap):
    return [''.join(['0'] * len(line)) for line in bitmap]


def to_bitmap(msg, size):
    font = {8: FONT_8, 16: FONT_16}[size]
    return Bitmap.concatall([font.glyph(ltr).draw()
                             for ltr in msg]).todata()
