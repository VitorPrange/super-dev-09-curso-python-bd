from mysql import connector
from dotenv import load_dotenv
import os


#carregar as variaveis definidas no .env
load_dotenv()


HOST = os.getenv("DB_HOST")
PORTA = os.getenv("DB_PORTA")
USUARIO = os.getenv("DB_USUARIO")
SENHA = os.getenv("DB_SENHA")
BANCO = os.getenv("DB_NOME")

def conectar():
    """Abre a conexão com MySQL e retorna ela"""
    conexao = connector.connect(
        host=HOST,
        port=PORTA,
        user=USUARIO,
        password=SENHA,
        database=BANCO,
    )
    return conexao