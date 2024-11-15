import banco_de_dados as bd
from Blueprits.funcionario import funcionario_funcoes
from Blueprits.medicamentos import medicamento_funcoes
from Blueprits.vendas import vendas_funcoes
from flask import Flask, render_template
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

sistema = Flask(__name__)
login_manager = LoginManager()
csrf = CSRFProtect(sistema)

sistema.config['SECRET_KEY'] = "Matheus"
csrf.init_app(sistema)

sistema.register_blueprint(funcionario_funcoes) # Estou dizendo que um dos meus sistemas de rotas fica no blueprint funcionario_funcoes
sistema.register_blueprint(medicamento_funcoes)  # Estou dizendo que um dos meus sistemas de rotas fica no blueprint medicamento_funcoes
sistema.register_blueprint(vendas_funcoes) # Estou dizendo que um dos meus sistemas de rotas fica no blueprint vendas_funcoes

sistema.run(debug = True)