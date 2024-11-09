from sqlalchemy import create_engine, Column, String, Integer, Float,Date,ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

banco_de_dados = create_engine("mysql:///medic_manager.db") #Crio a conexão com o bando de dados

Session = sessionmaker(bind=banco_de_dados) # Inicia uma sessão no banco de dados para modificá-lo (CRUD) 
session = Session() 

Tabelas = declarative_base() # É uma base que vou usar para criar as tabelas do banco de dados

class funcionario(Tabelas):
    __tablename__ = "Funcionario"

    id = Column("id",Integer, primary_key=True, autoincrement = True)
    nome = Column("nome",String)
    cpf = Column("cpf",Integer)
    data_nascimento = Column("data_nascimento",Date)
    telefone = Column("telefone", Integer)
    identificador = Column("identicador", Integer)
    senha = Column("senha", String)


class medicamento(Tabelas):
    __tablename__ = "Medicamento"

    id_medicamento = Column("id_medicamento",Integer, not_null = True,primary_key=True, autoincrement = True)
    nome_comercial = Column("nome_comercial",String)
    nome_generico = Column("nome_generico",String)
    codigo_identificacao = Column("codigo_identificacao", Integer)
    fabricante = Column("fabricante",String)
    embalagem = Column("embalagem",String)
    forma_farmaceutica = Column("forma_farmaceutica",String)
    quantidade_estoque = Column("quantidade_estoque",Integer)
    concentracao = Column("concentracao",String)
    preco = Column("preco",Float)
    dosagem = Column("dosagem",String)
    validade = Column("validade",Date)
    id_cadastror = Column("id_cadastrador",Integer, ForeignKey(funcionario.id))


class venda(Tabelas):
    id_medicamento = Column("id_medicamento",Integer,ForeignKey(medicamento.id_medicamento))
    quantidade_vendid = Column("quantidade_vendida",Integer)
    mes = Column("mes",Integer)
    id_funcionario = Column("id_funcionario",Integer,ForeignKey(funcionario.id))