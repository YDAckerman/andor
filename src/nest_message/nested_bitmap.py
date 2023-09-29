import re
from .utils import merge_str_lists, unlist, \
    make_circular, zero_out, to_bitmap
from ..html_shapes.html_shape import HtmlShape
import random

SPACE_CHAR = '&nbsp;'
COLORS = {"Yellow": '#ffd866',
          "Orange": '#fc9867',
          "Red": '#ff6188',
          "Green": '#a9dc76',
          "Blue": '#78dce8',
          "Purple": '#ab9df2',
          "Black": '#2c292d'}


class NestedBitmap():

    cir_seq = None

    def __init__(self, msg, size, pad=None, units=None, color=None):

        self.bitmap = to_bitmap(msg, size)
        self.size = size
        self.units = units

        if pad:
            self.pad_top(pad[0])
            self.pad_bottom(pad[1])

        if color:
            self.color = COLORS[color]
        else:
            self.color = random.choice(list(COLORS.values())[0:-1])

    def pad_top(self, space):
        self.bitmap = ['0' * self.get_bit_width() for _ in range(space)] \
            + self.bitmap

    def pad_bottom(self, space):
        self.bitmap = self.bitmap \
            + ['0' * self.get_bit_width() for _ in range(space)]

    def replace_bits(self, new_ones, invert=False):
        self._set_circular_sequencer(new_ones, invert)
        self.bitmap = unlist([self._replace_bits(line)
                              for line in self.bitmap])

    def print(self, remove_zero=False):

        def tmp(x):
            if remove_zero:
                return re.sub('0', ' ', x)
            return x

        print(tmp(self.bitmap[-1]))
        for line in self.bitmap:
            print(tmp(line))

    def get_bit_width(self):
        return len(self.bitmap[0])

    def get_bit_height(self):
        return len(self.bitmap)

    @classmethod
    def concat(cls, bm1, bm2):
        if bm1.get_bit_width() != bm2.get_bit_width():
            ValueError("NestedBitmat -> concat -> mismatched size")

        new_bm = cls(" ", bm1.size)
        new_bm.bitmap = bm1.bitmap + bm2.bitmap
        return new_bm

    def append(self, other):
        if self.get_bit_width() != other.get_bit_width():
            ValueError("NestedBitmat -> append -> mismatched width")
        self.bitmap = self.bitmap + other.bitmap

    def get_css_styles(self, r):

        bit_html = HtmlShape.generate_fixed_square(r, self.units, self.color)
        nobit_html = HtmlShape.generate_empty(r, self.units)

        def bit_to_style(i):
            if i != "0":
                return bit_html.get_style()
            return nobit_html.get_style()

        return [[bit_to_style(bit) for bit in bitline]
                for bitline in self.bitmap]

    def get_html_text(self, **kwargs):

        def sub_many(line):
            if kwargs:
                for item in kwargs.items():
                    line = re.sub(item[0], item[1], line)
            return re.sub("0", SPACE_CHAR, line)

        html_text = [sub_many(bitline) for bitline in self.bitmap]
        return html_text

    def _replace_bits(self, bitline):

        return merge_str_lists(*[self.cir_seq(int(bit))
                                 for bit in bitline])

    def _set_circular_sequencer(self, new_ones, invert):

        new_zero = zero_out(new_ones[0])
        new_ones = make_circular(new_ones)

        def rep_bit(i):
            if invert != bool(i):
                return next(new_ones)
            return new_zero

        self.cir_seq = rep_bit


def to_bitmap_html(r, units, pad_n, bits, msg, color=None):

    if color:
        color = COLORS[color]
    else:
        color = random.choice(list(COLORS.values())[0:-1])
    bit_msg = NestedBitmap(msg, bits)
    bit_msg.pad_top(pad_n)
    return bit_msg.get_css_styles(r, units, color)


def make_nested_msg(r, units, pad_n,
                    outer_bits, inner_bits,
                    outer_msg, inner_msg):

    color = random.choice(list(COLORS.values())[0:-1])

    bit_msg = NestedBitmap(outer_msg, outer_bits)
    bit_msg.pad_top(pad_n)
    nest_message = [NestedBitmap(ltr, inner_bits).bitmap
                    for ltr in inner_msg]
    bit_msg.replace_bits(nest_message, invert=True)
    bit_msg_css_styles = bit_msg.get_css_styles(r, units, color)
    bit_msg_width = bit_msg.get_bit_width() * r

    return bit_msg_width, bit_msg_css_styles


def main():

    tmp = NestedBitmap(" AND ", 16)
    tmp.replace_bits('OR', invert=False)
    tmp.print()

    tmp = NestedBitmap("  OR ", 16)
    tmp.replace_bits('AND', invert=True)
    tmp.print()

    tmp = NestedBitmap("H", 16)
    tmp.print()


if __name__ == '__main__':

    main()
