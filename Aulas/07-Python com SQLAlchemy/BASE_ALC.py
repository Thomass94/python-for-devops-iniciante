"""
  Nesse script criamos um objeto Base
  que vamos usar durante todo o nosso
  banco de dados.

  Modificado em 28 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

try:
    # engine = create_engine("sqlite:///banco.db")
    # engine = create_engine('mysql+mysqlconnector://root:root@localhost/projeto')
    engine = create_engine(
        'postgresql+psycopg2://postgres:123456@localhost/projeto',
        connect_args={'options': '-csearch_path=projeto'}
    )
    Base = declarative_base()
    print(engine)
    print(Base)
except Exception as e:
    print("Falhou a conexão %s" % e)
