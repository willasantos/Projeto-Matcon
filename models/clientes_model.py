from utils.clientes import Cliente
import  models.database as db

def getClientes():
    conn = db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * From clientes;")
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
    cursor.execute(sql, [id]) 
   
    linha = cursor.fetchall()[0]
     
    id = linha[0]
    nome = linha[1]
    cpf = linha[2]
    telefone = linha[3]
    email = linha[4]
    endereco = linha[5]
    #cria novo objeto
    novoCliente = Cliente(id, nome, cpf, telefone, email, endereco)
    conn.close()  
 
    return novoCliente  
    

def addCliente(cliente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO clientes (nome,cpf,telefone,email,endereco)
               VALUES (?, ?, ?, ?,?)"""
    cursor.execute(sql,[cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco])
    conn.commit()
    conn.close()
    

def editCliente(cliente):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE clientes SET nome=?, cpf=?, telefone=?, email=?, endereco=? WHERE id=? """
    cursor.execute(sql, [cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco, cliente.id])
    conn.commit()
    conn.close

def delCliente(id):
    conn= db.connect_db()
    cursor= conn.cursor()
    sql="""DELETE FROM clientes WHERE id = ?"""
    cursor.execute(sql, [id])
    conn.commit()
    conn.close() 
        
    
