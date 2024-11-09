class Medicamento:
    def __init__(self, nome_comercial, nome_generico, codigo_identificação
                 ,fabricante, embalagem, forma_farmaceutica, quantidade, concentracao,
                   preco,dosagem,validade, id_cadastro):
        self._id_medicamento = None
        self._nome_comercial = nome_comercial
        self._nome_generico = nome_generico
        self._codigo_identificacao = codigo_identificação
        self._fabricante = fabricante
        self._embalagem  = embalagem
        self._forma_farmaceutica = forma_farmaceutica
        self._quantidade_estoque = quantidade
        self._concentracao = concentracao
        self._preco = preco
        self._dosagem = dosagem
        self._validade = validade
        self._id_cadastror = id_cadastro

    @property
    def id_user_cadastro(self):
        return self.id_user_cadastro

    @property
    def nome_comercial(self):
        return self.nome_comercial
    
    @nome_comercial.setter
    def nome_comercial(self, nome_comercial):
        self._nome_comercial = nome_comercial

    @property
    def nome_generico(self):
        return self.nome_generico
    
    @nome_generico.setter
    def nome_comercial(self, nome_generico):
        self._nome_generico = nome_generico

    @property
    def codigo_identificacao(self):
        return self._codigo_identificacao
    
    @codigo_identificacao.setter
    def codigo_identificacao(self, codigo_identificacao):
        self._codigo_identificacao = codigo_identificacao

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

    @property
    def embalagem(self):
        return self.embalagem
    
    @embalagem.setter
    def embalagem(self, embalagem):
        self._embalagem = embalagem

    @property
    def forma_farmaceutica(self):
        return self._forma_farmaceutica
    
    @forma_farmaceutica.setter
    def forma_farmaceutica(self, forma_farmaceutica):
        self._forma_farmaceutica = forma_farmaceutica

    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque
    
    @quantidade_estoque.setter
    def quantidade_estoque(self, quantidade):
        self._quantidade_estoque = quantidade

    @property
    def forma_farmaceutica(self):
        return self._forma_farmaceutica
    
    @forma_farmaceutica.setter
    def forma_farmaceutica(self, forma_farmaceutica):
        self._forma_farmaceutica = forma_farmaceutica

    @property
    def concentracao(self):
        return self._concentracao
    
    @concentracao.setter
    def concentracao(self, concentracao):
        self._forma_farmaceutica = concentracao

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def dosagem(self):
        return self._dosagem
    
    @dosagem.setter
    def dosagem(self, dosagem):
        self._dosagem = dosagem

    @property
    def validade(self):
        return self._validade
    
    @validade.setter
    def validade(self, validade):
        self._validade = validade


    @property
    def id_cadastror(self):
        return self._id_cadastror
    
    def venda(self, quantidade):
        if quantidade <= self._quantidade_estoque:
            self._quantidade_estoque -= quantidade
        else:
            return "Valor acima da quantidade em estoque"


# medicamento1 = Medicamento(
#     nome_comercial="Paracetamol",
#     nome_generico="Paracetamol",
#     codigo_identificação="123456",
#     fabricante="Empresa Farmacêutica X",
#     embalagem="Caixa",
#     forma_farmaceutica="Comprimido",
#     quantidade=10,
#     concentracao="500mg",
#     preco=10.99,
#     dosagem="1 comprimido a cada 6 horas",
#     validade="31/12/2024",
#     id_cadastro="MED001"
# )
