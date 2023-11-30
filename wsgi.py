import os
from flask import Flask, render_template, request
from components.header import HEADER
from components.welcome import WELCOME
from components.messages import record_message
from components.fridge import get_magnets, update_magnets
from components.word_search import word_search
from src.db.db import init_app as db_init_app, get_conn
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'andor.db'),
)

db_init_app(app)


@app.route("/")
def index():
    return render_template("andor.html",
                           header=HEADER,
                           message=WELCOME)


@app.route("/andor", methods=['GET', 'POST'])
def andor():

    response = ["",""]

    if request.method == 'POST':
        get_conn()
        record_message(request.form)
        response = "message received!"

    return render_template("andor.html",
                           header=HEADER,
                           message=WELCOME,
                           response=response)


@app.route("/wordbefore", methods=['GET', 'POST'])
def wordbefore():

    response = ""

    if request.method == 'POST':
        word = request.form.get("word").upper()
        result = word_search(word)
        if len(result) == 1:
            response = [word + ":", "Yes, on " + result[0][0].split(", ")[1]]
        else:
            response = [word + ":", "Not a Wordle yet!!!"]

    return render_template("wordbefore.html",
                           header=HEADER,
                           response=response)

@app.route("/more")
def more():

    return render_template("more.html", header=HEADER)


@app.route("/acknowledgements")
def acknowledgements():

    return render_template("acknowledgements.html", header=HEADER)


@app.route("/fridge", methods=['GET', 'POST'])
def fridge():

    get_conn()

    if request.method == 'POST':
        update_magnets(request.form.items())

    magnets = get_magnets()
    return render_template("fridge.html",
                           header=HEADER,
                           magnets=magnets)
