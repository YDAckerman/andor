from .html_shape_templates import SHAPE_TEMPLATES
import math
import random

FADES = ["10_60"] * 3 + ["30_80"] * 10
MU_SIG = [3, 1]
DURATION = 20
COUNT = "infinite"


class HtmlShape:

    template = None

    def __init__(self, height, width, color, fade, duration, delay, count):
        self.height = height
        self.width = width
        self.color = color
        self.fade = fade
        self.duration = duration
        self.delay = delay
        self.count = count

    def set_template(self, template):
        self.template = template

    def get_style(self):
        if self.template:
            return self.template.format(h=self.height,
                                        w=self.width,
                                        c=self.color,
                                        fd=self.fade,
                                        du=self.duration,
                                        de=self.delay,
                                        n=self.count)
        ValueError("HtmlShape -> get_style -> template is None")

    def get_html(self):
        return "<div style=\"{}\"></div>".format(self.get_style())

    @staticmethod
    def random_params(px, color):
        r = px
        c = color
        du = DURATION
        de = min(abs(random.gauss(*MU_SIG)), 3)
        fd = random.choice(FADES)
        n = COUNT

        return [r, r, c, fd, du, de, n]

    @classmethod
    def random_circle(cls, px, color):

        inst = cls(*cls.random_params(px, color))
        inst.set_template(SHAPE_TEMPLATES['circle'])

        return inst

    @classmethod
    def random_square(cls, px, color):

        inst = cls(*cls.random_params(px, color))
        inst.set_template(SHAPE_TEMPLATES['square'])

        return inst

    @classmethod
    def blank_space(cls, px=1):

        r = px
        inst = cls(r, r, None, None, None, None, None)
        inst.set_template(SHAPE_TEMPLATES['blank'])

        return inst
