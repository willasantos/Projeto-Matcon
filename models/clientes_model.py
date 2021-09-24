# importar a classe cliente

from utils.clientes import Cliente
import  models.database as db

def getClientes():
    # crio a conexão
    conn = db.connect_db()
    # se comunica com o BD
    cursor = conn.cursor()
    # executa o comando de seleção dos clientes
    cursor.execute("SELECT * From clientes;")
    # coloca o resultado em uma lista de objetos clientes
    lista_clientes = []
    for linha in cursor.fetchall():
     
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
    # retorna ao novo cliente
    return lista_clientes  
    
# retorna um cliente específico
def getCliente(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """ SELECT * FROM clientes WHERE id = :"""
    cursor.execute(sql, [id]) # lista de argumentos na mesma ordem das ?s
   
     # erro quando não retorna nenhum cliente
    linha = cursor.fetchall()[0]
     
    id = linha[0]
    nome = linha[1]
    cpf = linha[2]
    telefone = linha[3]
    email = linha[4]
    endereco = linha[5]
    #cria novo objeto
    novoCliente = Cliente(id, nome, cpf, telefone, email, endereco)
    # insere o novo cliente na lista
    # fecha a conexão
    conn.close()  
    # retorna ao novo cliente
    return novoCliente  
    

def addCliente(cliente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Clientes (nome,cpf,telefone,email,endereco)
               VALEUS (?, ?, ?, ?,?):"""
    cursor.execute(sql,[cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco])
    conn.commit()
    conn.close()
    

def editCliente(cliente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE Clientes SET nome=?, cpf=?, telefone=?, email=?, endereco=? WHERE id=? """
    cursor.execute(sql, [cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco, cliente.id])
    conn.commit()
    conn.close

def delCliente(id):
    conn= db.connect_db()
    cursor= conn.cursor()
    sql="""DELETE FROM Clientes WHERE id=?"""
    cursor.execute(sql, [id])
    # grava os dados no banco de dados
    conn.commit()
    conn.close() 
        
    
