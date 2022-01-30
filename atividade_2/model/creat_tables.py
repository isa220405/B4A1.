# importa a blibioteca
from sqlalchemy import *
# importa modelos
from models import Jogador, Jogo, Federacao, Torneio
# conecta o banco de dados
engine = create_engine(
    "mysql+pymysql://root:@localhost/python?charset=utf8mb4", echo=True)

jogador = Jogador.__table__
jogador.create(engine, checkfirst=True)

jogo = Jogo.__table__
jogo.create(engine, checkfirst=True)

federacao = Federacao.__table__
federacao.create(engine, checkfirst=True)

torneio = Torneio.__table__
torneio.create(engine, checkfirst=True)
