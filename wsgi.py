import os
from flask import Flask, render_template, request
from components.header import HEADER
from components.message import MESSAGE
from components.fridge import get_magnets, update_magnets
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


@app.route("/andor")
@app.route("/")
def andor():

    return render_template("welcome.html",
                           header=HEADER,
                           message=MESSAGE)


@app.route("/more")
def more():

    return render_template("more.html", header=HEADER)


@app.route("/acknowledgements")
def acknowledgements():

    return render_template("acknowledgements.html", header=HEADER)


@app.route("/fridge", methods=['GET', 'POST'])
def fridge():

    if request.method == 'POST':

        def to_dict(k, v):
            word = k.split("_")[0]
            top, left = v.split("_")
            return {'word': word, 'top': top, 'left': left}

        data = [to_dict(k, v) for k, v in request.form.items()]
        update_magnets(data)

        return render_template("fridge.html", header=HEADER)
    else:
        get_conn()
        magnets = get_magnets()
        return render_template("fridge.html",
                               header=HEADER,
                               magnets=magnets)


@app.route("/send", methods=['POST'])
def send():

    return render_template("welcome.html",
                           header=HEADER,
                           message=MESSAGE)
