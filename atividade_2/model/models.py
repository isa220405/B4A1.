import datetime
from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.elements import collate
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import DECIMAL, INT, NVARCHAR, VARCHAR

Base = declarative_base()


class Jogador(Base):
    __tablename__ = 'jogador'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    codigo = Column(Integer, nullable=False)
    nome = Column(NVARCHAR(45), nullable=False)
    titulo = Column(NVARCHAR(45), nullable=False)
    nacionalidade = Column(NVARCHAR(45), unique=True, nullable=False)
    rating = Column(Integer, nullable=False)


class Jogo(Base):
    __tablename__ = 'jogo'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    id_jogador = Column(Integer, ForeignKey('jogador.id'))
    id_adversario = Column(Integer, ForeignKey('jogador.id'))
    nome_abertura = Column(NVARCHAR(45), nullable=False)
    numero_lances = Column(Integer, nullable=False)
    resultado = Column(Integer, nullable=False)


class Federacao(Base):
    __tablename__ = 'federacao'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nome = Column(NVARCHAR(45), nullable=False)
    idade = Column(Integer, nullable=False)


class Torneio(Base):
    __tablename__ = 'torneio'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    id_jogador = Column(Integer, ForeignKey('jogador.id'))
    id_federacao = Column(Integer, ForeignKey('torneio.id'))
    id_jogo = Column(Integer, ForeignKey('jogo.id'))
    pontos = Column(Integer, nullable=False)
    posicao = Column(Integer, nullable=False)
    titulo_possivel = Column(NVARCHAR(45), nullable=False)
