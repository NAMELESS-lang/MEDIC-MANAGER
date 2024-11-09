from flask import Flask

sistema = Flask(__name__)


@sistema.route("/")
def sucesso():
    return f"<p>ok</p>"




sistema.run(debug=True)