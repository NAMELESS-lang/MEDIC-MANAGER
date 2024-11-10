from flask import Blueprint, render_template

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

    def setar_identificador(self):
        import random
        if self._identificador == "":
            nums = [i for i in range(0,11)]
            for numero in range(0,8):
                numero = str(random.choice(nums))
                self._identificador += numero
            self._identificador = int(self._identificador)
            return
        raise ValueError


# Associo rotas a este meu blueprint

@funcionario_funcoes.route("/")
def comece():
    render_template("cadastro.html")

@funcionario_funcoes.route("/cadastro")
def cadastro():
    return "<p>foi para cadastro</p>"


# pessoa = Funcionario("Marilene",25434892000,"24/09/2018","(55)98133-4456","Olá")
# pessoa.setar_identificador()
