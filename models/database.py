import sqlite3

URL_DATABASE = 'models/Bancodedados.db'

def connect_db():
    # cria a conexão
    conn = sqlite3.connect(URL_DATABASE)
    return conn