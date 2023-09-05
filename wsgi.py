from flask import Flask
from flask import render_template
from src.nest_message.nested_bitmap import to_bit_msg
import re
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)


# @app.route("/")
# def index():

#     MSG_PADDING = 1
#     INNER_BITS = 8
#     OUTER_BITS = 8
#     VW = .22
#     INNER_MSG = 'OR'
#     OUTER_MSG = ' AND '
#     ANIMATION_COUNT = "inifite"
#     ANIMATION_EFFECT = "blink"

#     bit_msg_width, bit_msg_css_styles = to_bit_msg(VW,
#                                                    MSG_PADDING,
#                                                    OUTER_BITS,
#                                                    INNER_BITS,
#                                                    OUTER_MSG,
#                                                    INNER_MSG,
#                                                    ANIMATION_COUNT,
#                                                    ANIMATION_EFFECT)

#     return render_template("index.html",
#                            bit_msg_styles=bit_msg_css_styles,
#                            bit_msg_width=bit_msg_width
#                            )


@app.route("/about")
@app.route("/")
def about():

    MSG_PADDING = 2
    INNER_BITS = 8
    OUTER_BITS = 16
    VW = .15
    OUTER_MSG = ' Hi '
    ANIMATION_COUNT = "1"
    ANIMATION_EFFECT = "fixed"

    with open("./static/about_content/about_message.txt") as f:
        INNER_MSG = re.sub("\n", " ", f.read())

    bit_msg_width, bit_msg_css_styles = to_bit_msg(VW,
                                                   MSG_PADDING,
                                                   OUTER_BITS,
                                                   INNER_BITS,
                                                   OUTER_MSG,
                                                   INNER_MSG,
                                                   ANIMATION_COUNT,
                                                   ANIMATION_EFFECT)

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/projects")
def projects():

    MSG_PADDING = 1
    INNER_BITS = 8
    OUTER_BITS = 8
    VW = .15
    INNER_MSG = 'UGH!'
    OUTER_MSG = ' 404 '
    ANIMATION_COUNT = "1"
    ANIMATION_EFFECT = "fixed"

    bit_msg_width, bit_msg_css_styles = to_bit_msg(VW,
                                                   MSG_PADDING,
                                                   OUTER_BITS,
                                                   INNER_BITS,
                                                   OUTER_MSG,
                                                   INNER_MSG,
                                                   ANIMATION_COUNT,
                                                   ANIMATION_EFFECT)

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/notes")
def notes():

    MSG_PADDING = 1
    INNER_BITS = 8
    OUTER_BITS = 16
    VW = .10
    INNER_MSG = 'WHOOPS!'
    OUTER_MSG = ' um '
    ANIMATION_COUNT = "1"
    ANIMATION_EFFECT = "fixed"

    bit_msg_width, bit_msg_css_styles = to_bit_msg(VW,
                                                   MSG_PADDING,
                                                   OUTER_BITS,
                                                   INNER_BITS,
                                                   OUTER_MSG,
                                                   INNER_MSG,
                                                   ANIMATION_COUNT,
                                                   ANIMATION_EFFECT)

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )


@app.route("/designs")
def designs():

    MSG_PADDING = 1
    INNER_BITS = 8
    OUTER_BITS = 16
    VW = .10
    INNER_MSG = 'OY'
    OUTER_MSG = ' VEY! '
    ANIMATION_COUNT = "1"
    ANIMATION_EFFECT = "fixed"

    bit_msg_width, bit_msg_css_styles = to_bit_msg(VW,
                                                   MSG_PADDING,
                                                   OUTER_BITS,
                                                   INNER_BITS,
                                                   OUTER_MSG,
                                                   INNER_MSG,
                                                   ANIMATION_COUNT,
                                                   ANIMATION_EFFECT)

    return render_template("index.html",
                           bit_msg_styles=bit_msg_css_styles,
                           bit_msg_width=bit_msg_width
                           )
