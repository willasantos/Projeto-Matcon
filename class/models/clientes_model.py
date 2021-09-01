#Importar a classe cliente
from class.clientes import  Cliente 

import sqlite3
    

# Pega todos os clientes do banco de dados
def getClientes():
    # cria a conexão
    conn = sqlite3.connect('models/Banco de dados.sqbpro')
    # se comunicar com o BD
    cursor = conn.cursor()
    # executa o comando de seleção dos clientes
    cursor.execute("""SELECT + FROM clientes;""")
    #imprimr o resultado
    for linha in cursor.fetchall():
        id = linha[0]
        nome = linha[1]
        cpf = linha[2]
        telefone = linha[3]
        email = linha[4]
        endereco = linha[5]
        novoCliente= Cliente(id, nome, cpf, telefone, email, endereco)
        lista_clientes.append(novoCliente)
        print(linha)
     
      # fecha conexão
    conn.close()   
    return lista_clientes 


  

def getCliente(id):    
    
    print("retorna um cliente específico")

def addCliente(cliente):
    print("Novo cliente os campos do cliente")

def editCliente(cliente):
    print("Edita um cliente os campos do cliente")

def delCliente(id):
    print("Deleta um cliente específico")            