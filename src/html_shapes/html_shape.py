from .html_shape_templates import SHAPE_TEMPLATES


class HtmlShape:

    template = None

    def __init__(self, height, width, units, color=None):

        self.height = height
        self.width = width
        self.units = units
        self.color = color

    def set_template(self, template):
        self.template = template

    def get_style(self):
        if self.template:
            return self.template.format(h=self.height,
                                        w=self.width,
                                        c=self.color,
                                        u=self.units)
        ValueError("HtmlShape -> get_style -> template is None")

    def get_html(self):
        return "<div style=\"{}\"></div>".format(self.get_style())

    @classmethod
    def generate_fixed_square(cls, r, u, c):

        inst = cls(r, r, u, c)
        inst.set_template(SHAPE_TEMPLATES['square_fixed'])

        return inst

    @classmethod
    def generate_empty(cls, r, u):

        inst = cls(r, r, u)
        inst.set_template(SHAPE_TEMPLATES['empty'])

        return inst
