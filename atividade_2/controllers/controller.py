
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc
from model.models import Jogador, Jogo, Federacao, Torneio

engine = create_engine("mysql+pymysql://root:@localhost/python", echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def jogador(codigo, nome, titulo, nacionalidade, rating):
    jogador = Jogador(codigo=codigo, nome=nome, titulo=titulo,
                      nacionalidade=nacionalidade, rating=rating)
    session.add(jogador)
    session.commit()


def jogo(id_jogador, id_adversario, nome_abertura, numero_lances, resultado):
    jogo = Jogo(id_jogador=id_jogador, id_adversario=id_adversario,
                nome_abertura=nome_abertura, numero_lances=numero_lances, resultado=resultado)
    session.add(jogo)
    session.commit()


def federacao(nome, idade):
    federacao = Federacao(nome=nome, idade=idade)
    session.add(federacao)
    session.commit()


def torneio(id_jogador, id_federacao, id_jogo, pontos, posicao, titulo_possivel):
    torneio = Torneio(id_jogador=id_jogador, id_federacao=id_federacao, id_jogo=id_jogo,
                      pontos=pontos, posicao=posicao, titulo_possivel=titulo_possivel)
    session.add(torneio)
    session.commit()
