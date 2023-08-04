from flask import Flask
from flask import render_template
from src.nest_message.nested_bitmap import nested_bit_msg, NestedBitmap


app = Flask(__name__)


@app.route("/")
def index():

    bit_msg_width, bit_msg_css_styles = nested_bit_msg(.22, 8, ' AND ', 'OR')

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

    bit_msg_width, bit_msg_css_styles = nested_bit_msg(.15, 8,
                                                       ' COMING ', 'SOON')

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/notes")
def notes():

    bit_msg_width, bit_msg_css_styles = nested_bit_msg(.15, 8,
                                                       ' COMING ', 'SOON')

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/designs")
def designs():

    bit_msg_width, bit_msg_css_styles = nested_bit_msg(.15, 8,
                                                       ' COMING ', 'SOON')

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )
