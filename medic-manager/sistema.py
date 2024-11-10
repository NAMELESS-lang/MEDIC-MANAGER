from flask import Flask,render_template
from flask_login import LoginManager

sistema = Flask(__name__)
login_manager = LoginManager()

@sistema.route("/")
def login():
    return render_template("login.html")


@sistema.route("/login", methods = ["POST"])
def sucesso():
    return "<p>Ok</p>"


sistema.run(debug = True)
