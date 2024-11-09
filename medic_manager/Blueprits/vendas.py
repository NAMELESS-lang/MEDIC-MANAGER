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