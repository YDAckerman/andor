import os
from flask import Flask
from flask import render_template
from components.header import HEADER
from components.message import MESSAGE
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'andor.sqlite'),
    )


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


@app.route("/send", methods=['POST'])
def send():

    return render_template("welcome.html",
                           header=HEADER,
                           message=MESSAGE)
