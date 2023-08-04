from flask import Flask
from flask import render_template
from src.nest_message.nested_bitmap import NestedBitmap
import random

app = Flask(__name__)

COLORS = ["Yellow", "Orange", "Red", "Green", "Blue", "Purple"]
SHAPES = ["circle", "square"]


@app.route("/")
def index():

    SHAPE_VW = .22
    FONT_BITS = 8
    MSG_PADDING = 1
    SHAPE = random.choice(SHAPES)
    COLOR = random.choice(COLORS)

    bit_msg = NestedBitmap(' AND ', FONT_BITS)
    bit_msg.pad_top(MSG_PADDING)
    nest_message = [NestedBitmap(ltr, FONT_BITS).bitmap
                    for ltr in 'OR']
    bit_msg.replace_bits(nest_message, invert=True)
    bit_msg_css_styles = bit_msg.get_css_styles(SHAPE,
                                                SHAPE_VW,
                                                COLOR)
    bit_msg_width = bit_msg.get_bit_width() * SHAPE_VW

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/about")
def about():

    MSG_PADDING = 1
    FONT_BITS = 8

    with open("./static/about_content/about_message.txt") as f:
        about_msg = f.read()

    msg = NestedBitmap(' Hi ', FONT_BITS)
    msg.pad_top(MSG_PADDING)
    msg.replace_bits([["11", "11"]], invert=True)
    msg.replace_bits(about_msg)
    text_lines = msg.get_html_text(github_here='github <a '
                                   + 'href="https://github.com/YDAckerman/"'
                                   + 'target="_blank" '
                                   + 'style="color: #78dce8;">here</a>')

    return render_template("index.html",
                           text_lines=text_lines)


@app.route("/projects")
def projects():

    SHAPE_VW = .2
    FONT_BITS = 8
    MSG_PADDING = 1
    SHAPE = random.choice(SHAPES)
    COLOR = random.choice(COLORS)

    bit_msg = NestedBitmap.concat(NestedBitmap(' COM ', FONT_BITS),
                                  NestedBitmap(' ING ', FONT_BITS))
    bit_msg.pad_top(MSG_PADDING)
    nest_message = [NestedBitmap(ltr, FONT_BITS).bitmap
                    for ltr in 'SOON']
    bit_msg.replace_bits(nest_message, invert=True)
    bit_msg_css_styles = bit_msg.get_css_styles(SHAPE,
                                                SHAPE_VW,
                                                COLOR)
    bit_msg_width = bit_msg.get_bit_width() * SHAPE_VW

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/notes")
def notes():

    SHAPE_VW = .2
    FONT_BITS = 8
    MSG_PADDING = 1
    SHAPE = random.choice(SHAPES)
    COLOR = random.choice(COLORS)

    bit_msg = NestedBitmap.concat(NestedBitmap(' COM ', FONT_BITS),
                                  NestedBitmap(' ING ', FONT_BITS))
    bit_msg.pad_top(MSG_PADDING)
    nest_message = [NestedBitmap(ltr, FONT_BITS).bitmap
                    for ltr in 'SOON']
    bit_msg.replace_bits(nest_message, invert=True)
    bit_msg_css_styles = bit_msg.get_css_styles(SHAPE,
                                                SHAPE_VW,
                                                COLOR)
    bit_msg_width = bit_msg.get_bit_width() * SHAPE_VW

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/designs")
def designs():

    SHAPE_VW = .2
    FONT_BITS = 8
    MSG_PADDING = 1
    SHAPE = random.choice(SHAPES)
    COLOR = random.choice(COLORS)

    bit_msg = NestedBitmap.concat(NestedBitmap(' COM ', FONT_BITS),
                                  NestedBitmap(' ING ', FONT_BITS))
    bit_msg.pad_top(MSG_PADDING)
    nest_message = [NestedBitmap(ltr, FONT_BITS).bitmap
                    for ltr in 'SOON']
    bit_msg.replace_bits(nest_message, invert=True)
    bit_msg_css_styles = bit_msg.get_css_styles(SHAPE,
                                                SHAPE_VW,
                                                COLOR)
    bit_msg_width = bit_msg.get_bit_width() * SHAPE_VW

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )
