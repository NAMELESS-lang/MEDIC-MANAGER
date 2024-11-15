import banco_de_dados as bd
from Blueprits.funcionario import funcionario_funcoes
from Blueprits.medicamentos import medicamento_funcoes
from Blueprits.vendas import vendas_funcoes


from flask import Flask, render_template
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


def secret_key_setar():
    """
    Função que irá gerar uma SECRET_KEY aleatória toda vez que o sistema for iniciado, acho útil deste jeito por questões de segurança,
    visto que a chave sempre vai ser aleatória.
    """
    import random
    chave = ""
    nums = [i for i in range(0,10)]
    for numero in range(0,8):
        numero = str(random.choice(nums))
        chave += numero
    return chave

""" Configurações do sistema"""
sistema = Flask(__name__)
login_manager = LoginManager()
csrf = CSRFProtect(sistema)
sistema.config['SECRET_KEY'] = secret_key_setar()
csrf.init_app(sistema)
login_manager.init_app(sistema)


""" Toda vez que uma requisição é realizada o este endpoint é chamado pelo flask_login para ver se o usuário que está logado existe no banco de dados."""
@login_manager.user_loader 
def load_user(user_id): 
    from Blueprits.funcionario import Funcionario
    funcionario = bd.buscar_por_id(user_id)
    # Preciso retornar um objeto da classe, pois ela esta herdando de UserMixin que contém o is_authenticated
    if funcionario:
       return Funcionario(funcionario.id, funcionario.nome, funcionario.cpf, funcionario.data_nascimento, funcionario.telefone,funcionario.identificador)

""" Definindo os Blueprints"""
sistema.register_blueprint(funcionario_funcoes) # Estou dizendo que um dos meus sistemas de rotas fica no módulo funcionario
sistema.register_blueprint(medicamento_funcoes)  # Estou dizendo que um dos meus sistemas de rotas fica no módulo medicamento
sistema.register_blueprint(vendas_funcoes) # Estou dizendo que um dos meus sistemas de rotas fica no módulo vendas

sistema.run(debug = True)