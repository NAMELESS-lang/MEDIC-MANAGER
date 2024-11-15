
from sqlalchemy import create_engine, Column, String, Integer, Float,Date,ForeignKey,VARCHAR
from sqlalchemy.orm import sessionmaker, declarative_base

banco_de_dados = create_engine("mysql+pymysql://root:1234@localhost:3306/medic_manager") #Crio a conexão com o bando de dados
banco_de_dados.connect()
Session = sessionmaker(bind=banco_de_dados) # Inicia uma sessão no banco de dados para modificá-lo (CRUD) 
session = Session() 

Tabelas = declarative_base() # É uma base que vou usar para criar as tabelas do banco de dados
    
class funcionario(Tabelas):
    __tablename__ = "Funcionario"

    id = Column("id",Integer, primary_key=True, autoincrement = True)
    nome = Column("nome",String(30))
    cpf = Column("cpf",VARCHAR(14))
    data_nascimento = Column("data_nascimento",Date)
    telefone = Column("telefone", VARCHAR(15))
    identificador = Column("identicador", VARCHAR(8))
    senha = Column("senha", VARCHAR(200))



class medicamento(Tabelas):
    __tablename__ = "Medicamento"

    id_medicamento = Column("id_medicamento",Integer,primary_key=True, autoincrement = True)
    nome_comercial = Column("nome_comercial",String(50))
    nome_generico = Column("nome_generico",String(50))
    codigo_identificacao = Column("codigo_identificacao", Integer)
    fabricante = Column("fabricante",String(30))
    embalagem = Column("embalagem",String(20))
    forma_farmaceutica = Column("forma_farmaceutica",String(20))
    quantidade_estoque = Column("quantidade_estoque",Integer)
    concentracao = Column("concentracao",String(10))
    preco = Column("preco",Float)
    dosagem = Column("dosagem",String(30))
    validade = Column("validade",Date)
    id_cadastror = Column("id_cadastrador",Integer, ForeignKey(funcionario.id))


class venda(Tabelas):
    __tablename__ = "Venda"

    id_da_venda = Column("id_da_venda",Integer, primary_key=True)
    id_medicamento = Column("id_medicamento",Integer,ForeignKey(medicamento.id_medicamento))
    quantidade_vendid = Column("quantidade_vendida",Integer)
    mes = Column("mes",Integer)
    id_funcionario = Column("id_funcionario",Integer,ForeignKey(funcionario.id))

Tabelas.metadata.create_all(bind=banco_de_dados)