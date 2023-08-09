from flask import Flask
from flask import render_template
from src.nest_message.nested_bitmap import to_bit_msg
import re

app = Flask(__name__)


@app.route("/")
def index():

    bit_msg_width, bit_msg_css_styles = to_bit_msg(.22, 1, 8, 8,
                                                   ' AND ', 'OR',
                                                   "infinite",
                                                   "blink")

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/about")
def about():

    MSG_PADDING = 2
    FONT_BITS = 16
    VW = .15

    with open("./static/about_content/about_message.txt") as f:
        about_msg = re.sub("\n", " ", f.read())

    # msg = NestedBitmap(' Hi ', FONT_BITS)
    # msg.pad_top(MSG_PADDING)
    # # msg.replace_bits([["11", "11"]], invert=True)
    # nest_msg = [NestedBitmap(ltr, 8).bitmap for ltr in about_msg]
    # msg.replace_bits(nest_msg, invert=True)
    # styles = msg.get_css_styles("square", VW, "Blue")
    # width = msg.get_bit_width() * VW

    # return render_template("index.html",
    #                        bit_msg_styles=styles,
    #                        bit_msg_width=width)


    bit_msg_width, bit_msg_css_styles = to_bit_msg(.15, 2, 16, 8,
                                                   ' Hi ',
                                                   about_msg,
                                                   "1",
                                                   "fixed"
                                                   )

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/projects")
def projects():

    bit_msg_width, bit_msg_css_styles = to_bit_msg(.15, 1, 8, 8,
                                                   ' COMING ',
                                                   'SOON',
                                                   "infinite",
                                                   "blink"
                                                   )

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/notes")
def notes():

    bit_msg_width, bit_msg_css_styles = to_bit_msg(.15, 1, 8, 8,
                                                   ' COMING ',
                                                   'SOON',
                                                   "infinite",
                                                   "blink"
                                                   )

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/designs")
def designs():

    bit_msg_width, bit_msg_css_styles = to_bit_msg(.15, 1, 8, 8,
                                                   ' COMING ',
                                                   'SOON',
                                                   "infinite",
                                                   "blink"
                                                   )

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )
