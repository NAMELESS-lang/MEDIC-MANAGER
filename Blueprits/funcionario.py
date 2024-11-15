import banco_de_dados as db
from flask import Blueprint, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TelField,DateField
from wtforms.validators import DataRequired
from flask_bcrypt import Bcrypt
gerador_senha = Bcrypt()
funcionario_funcoes = Blueprint("funcionario_funcoes", __name__) #Digo que este meu script é um blueprint que vai conter as funções(rotas/views) relacionadas aos funcionários

class Funcionario:
    def __init__(self,nome:str,cpf:int,data_nascimento:str, telefone:int,senha:str):
        self._id = None
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento
        self._telefone = telefone
        self._identificador  = ""
        self._senha = senha

    @property
    def id (self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def identificador(self):
        return self._identificador
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self,senha):
        self._senha = senha

class Formulario_cadastro(FlaskForm):
    """
    Crie este formulário de cadastro usando o flask-WTF por que queria entender o funcionamento desta biblioteca, além de já vir com 
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
    Usei um sistema de identificação, pois criei um sistema baseando-se em que o mesmo fosse usado em um ambiente como um hospital
    e creio que um número identificador seja mais conveniente usar para acesso e também por quesitos de segurança.
    """

    identificador = StringField('Identificador', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])


def setar_identificador():
        import random
        identificador = ""
        nums = [i for i in range(0,10)]
        for numero in range(0,8):
            numero = str(random.choice(nums))
            identificador += numero
        identificador = int(identificador)
        return identificador

# Associo rotas a este meu blueprint

@funcionario_funcoes.route("/cadastro_funcionario_pagina")
def cadastro():
    formulario = Formulario_cadastro()
    return render_template("cadastro.html",formulario = formulario)
    
@funcionario_funcoes.route("/funcionario_cadastrar-se",methods=["POST"])
def cadastrar_se():
        formulario = Formulario_cadastro()
        if formulario.validate_on_submit():
            senha = gerador_senha.generate_password_hash(formulario.senha._value())
            Usuario_cadastro = db.funcionario(nome = formulario.nome._value(), cpf = formulario.cpf._value(), data_nascimento = formulario.data_nascimento._value(), 
                                              telefone = formulario.telefone._value(), identificador = setar_identificador(), senha = senha)
            db.session.add(Usuario_cadastro)
            db.session.commit()
            return "<p> Usuário cadastrado com sucesso!</p>"
        

@funcionario_funcoes.route('/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        formulario = Formulario_login()
        return render_template('login.html', formulario = formulario)
    else:
       return '<p>Ok</p>'