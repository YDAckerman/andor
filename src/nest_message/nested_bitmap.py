import re
from .utils import merge_str_lists, unlist, \
    make_circular, zero_out, to_bitmap
from ..html_shapes.html_shape import HtmlShape


SHAPE_FUNS = {
    "square": HtmlShape.random_square,
    "circle": HtmlShape.random_circle,
    "blank": HtmlShape.blank_space
}

SPACE_CHAR = '&nbsp;'


class NestedBitmap():

    cir_seq = None

    def __init__(self, msg, size):

        self.bitmap = to_bitmap(msg, size)
        self.size = size

    def pad_top(self, space):
        self.bitmap = [self.bitmap[-1] for _ in range(space)] \
            + self.bitmap

    def pad_bottom(self, space):
        self.bitmap = self.bitmap \
            + [self.bitmap[-1] for _ in range(space)]

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
        if bm1.size != bm2.size:
            ValueError("NestedBitmat -> concat -> mismatched size")

        new_bm = cls(" ", bm1.size)
        new_bm.bitmap = bm1.bitmap + bm2.bitmap
        return new_bm

    def get_css_styles(self, shape, px, color):

        def bit_to_style(i):
            if i != "0":
                return SHAPE_FUNS[shape](px, color).get_style()
            return SHAPE_FUNS["blank"](px).get_style()

        return [bit_to_style(bit)
                for bitline in self.bitmap for bit in bitline]

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


def main():

    tmp = NestedBitmat(" AND ", 16)
    tmp.replace_bits('OR', invert=False)
    tmp.print()

    tmp = NestedBitmat("  OR ", 16)
    tmp.replace_bits('AND', invert=True)
    tmp.print()


if __name__ == '__main__':

    main()
