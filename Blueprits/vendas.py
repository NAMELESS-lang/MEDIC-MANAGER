from flask import Blueprint

vendas_funcoes = Blueprint("vendas_funcoes", __name__) #Digo que este meu script é um blueprint que vai conter as funções(rotas/views) relacionadas a vendas


class Vendas:
    def __init__(self,id_medicamento, quantidade_vendida, mes,id_funcionario):
        self._id_medicamento = id_medicamento
        self._quantidade_vendida = quantidade_vendida
        self._mes = mes
        self._id_funcionario = id_funcionario
    
    @property
    def quantidade_vendida(self):
        return self._quantidade_vendida
    
    @property
    def mes(self):
        return self._mes