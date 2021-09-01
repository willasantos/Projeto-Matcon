# importat a classe cliente

from utils.clientes import Cliente
import sqlite3

def getClientes():
    # crio a conexão
    conn = sqlite3.connect('models/db_Banco de dados.db')
    # se comunica com o BD
    cursor = conn.cursor()
    cursor.execute("SELECT * From clientes;")

    for linha in cursor.fetchall():
        print(linha)

    conn.close()    


def getCliente(id):
    print("retorna um cliente específico")

def addCliente(cliente):
    print("novo cliente os campos do clientes")

def editCliente(cliente):
    print("edita um cliente os campos do cliente")    

def delCliente(id):
    print("Deleta um cliente específico")    
