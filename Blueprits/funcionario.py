
import banco_de_dados as db
from flask import Blueprint, render_template, url_for, request
from flask_login import UserMixin, login_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField,DateField
from wtforms.validators import DataRequired
from flask_bcrypt import Bcrypt

""" Instâncio um objeto bcrypt para criptografia e defino meu blueprint"""
gerador_senha = Bcrypt()
funcionario_funcoes = Blueprint("funcionario_funcoes", __name__) #Digo que este meu script é um blueprint que vai conter as funções(rotas/views) relacionadas aos funcionários

class Funcionario(UserMixin):

    """
    Esta classe é responsável por criar o usuário que estára logado durante o uso do sistema. Ela herda de UserMixin, pois é necessária
    para permitir ao flask_login verificar se o usuário está logado.
    """
    def __init__(self,id:int,nome:str,cpf:int,data_nascimento:str, telefone:int, identificador:str):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._telefone = telefone
        self._identificador  = identificador
        self._ativo = False
    
    @property 
    def id(self): return self._id

    def get_id(self): return self._id

    @property
    def nome(self):  return self._nome
    
    @nome.setter
    def nome(self, nome): self._nome = nome

    @property
    def cpf(self): return self._cpf
    
    @cpf.setter
    def cpf(self, cpf): self._cpf = cpf

    @property
    def telefone(self): return self._telefone
    
    @telefone.setter
    def telefone(self, telefone): self._telefone = telefone

    @property
    def identificador(self): return self._identificador
    
    def ativar_funcionario(self): 
        self._ativo = True 

class Formulario_cadastro(FlaskForm):
    """
    Criei este formulário de cadastro usando o flask-WTF por que queria entender o funcionamento desta biblioteca, além de já vir com 
    recursos de segurança para os formulários

    O validators serve para validar os campos, por exemplo, invalidar se o campo for nulo ou se as informações
    preenchiadas são incorretas
    """
    nome = StringField('Nome',validators=[DataRequired()]) 
    cpf = StringField('CPF', validators=[DataRequired()])
    data_nascimento = DateField('Data de nascimento', validators=[DataRequired()])
    telefone = TelField('Telefone', validators=[DataRequired()])
    senha = PasswordField('Senha',validators=[DataRequired()])

class Formulario_login(FlaskForm):

    """ 
    Usei um sistema que solicita identificação, pois baseio-se que este sistema fosse usado em um ambiente como um hospital,
    e creio que um número identificador seja mais conveniente usar para acesso, e também por questões de segurança.
    """

    identificador = StringField('Identificador', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])


def setar_identificador():
        
    """
    Criei este gerador de identificador aleatório, pois acho que há mais segunça no sistema fornecendo números aleatórios, e não uma sequência pré-definida.
    """
    import random
    identificador = ""
    nums = [i for i in range(0,10)]
    for numero in range(0,8):
        numero = str(random.choice(nums))
        identificador += numero
    identificador = int(identificador)
    return identificador



@funcionario_funcoes.route("/cadastro_funcionario_pagina")
def cadastro():
    formulario = Formulario_cadastro() # Crio um formulário
    return render_template("cadastro.html",formulario = formulario) # Envio ele para a página de cadastro


@funcionario_funcoes.route("/funcionario_cadastrar-se",methods=["POST"])
def cadastrar_se():
        """ Crio um objeto formulário_cadastro que vai assimilar as informações vindas do request"""
        formulario = Formulario_cadastro()
        
        """ Faço a validação dos campos e se tudo estiver correto criptografo o campo da senha e insiro o funcionário no banco de dados"""
        if formulario.validate_on_submit(): # Valida os dados
            senha = gerador_senha.generate_password_hash(formulario.senha._value()).decode("utf-8") # Criptografa a senha
            Usuario_cadastro = db.funcionario(nome = formulario.nome._value(), cpf = formulario.cpf._value(), data_nascimento = formulario.data_nascimento._value(), 
                                              telefone = formulario.telefone._value(), identificador = setar_identificador(), senha = senha)
            db.session_CRUD.add(Usuario_cadastro)
            db.session_CRUD.commit()
            return "<p> Usuário cadastrado com sucesso!</p>"
        

@funcionario_funcoes.route('/', methods=['GET','POST'])
def login():
    """ 
    Se o request for GET envio o usuário para a página de login com o formulário de login.
    Se for POST é porque o usuário está tentando logar e por isso realizo o processo de login   
    """
    try:
        if request.method == 'GET':
            formulario = Formulario_login()
            return render_template('login.html', formulario = formulario)
        else:
            """
            Aqui começa o POST, valido os dados e em seguida busco o usuário no banco de dados pelo identificador senão o encontrar retorna para a página de login notificando
            ao usuário de que não foi encontrado no sistema. Já se encontrá-lo verifica se a senha digitada e a do retorno for a mesma, realiza o login, senão redireciona para a página de 
            login e notifica que a senha está incorreta.
            """
            formulario = Formulario_login()
            if formulario.validate_on_submit(): # Valida os dados
                identificador = formulario.identificador._value()
                senha = formulario.senha._value()
                funcionario = db.buscar_por_identificador(identificador)
                if funcionario: # Se o funcionário foi encontrado no banco de dados
                    if gerador_senha.check_password_hash(funcionario.senha, senha): # Se as senhas coincidem
                        funcionario_logado = Funcionario(funcionario.id, funcionario.nome, funcionario.cpf, 
                                                            funcionario.data_nascimento, funcionario.telefone, funcionario.identificador)
                        funcionario_logado.ativar_funcionario()
                        login_user(funcionario_logado, remember=True) # Loga o usuário
                        return f"<p> Usuario logado {funcionario.nome}, {funcionario.identificador}</p>" # Usuário logado
                    else:
                        return f"<p>Senha incorreta!</p>" # Senha incorreta
                else:
                    return f"<p> Usuário não encontrado na base de dados do sistema!" # Não encontrado no sistema
    except Exception as erro: # Captura alguma excessão
        print(erro)
@funcionario_funcoes.route('/teste')
@login_required
def ola():
    return f"<p>deu certo!</p>"


    
