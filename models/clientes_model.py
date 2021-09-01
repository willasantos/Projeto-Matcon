# importat a classe cliente

from utils.clientes import Cliente
import sqlite3

def getClientes():
    # crio a conexão
    conn = sqlite3.connect('models/Bancodedados.db')
    # se comunica com o BD
    cursor = conn.cursor()
    # executa o comando de seleção dos clientes
    cursor.execute("""SELECT * From clientes;""")
    # coloca o resultado em uma lista de objetos clientes
    lista_clientes = []
    for linha in cursor.fetchall():
        print(linha)
        id = linha[0]
        nome = linha[1]
        cpf = linha[2]
        telefone = linha[3]
        email = linha[4]
        endereco = linha[5]
        #cria novo objeto
        novoCliente = Cliente(id, nome, cpf, telefone, email, endereco)
        # insere o novo cliente na lista
        lista_clientes.append(novoCliente)
     # fecha a conexão
    conn.close()  
     # retorna a lista  
    return lista_clientes

def getCliente(id):
    
    print("retorna um cliente específico")

def addCliente(cliente):
    print("novo cliente os campos do clientes")

def editCliente(cliente):
    print("edita um cliente os campos do cliente")    

def delCliente(id):
    print("Deleta um cliente específico")    
