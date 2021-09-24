
from utils.produtos import Produto
import models.database as db

def getProdutos():
    conn= db.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos; ")

    lista_produtos = []
    """ for s in cursor.fetchall():
       # id = s[0]
        #nome = s[1]
        marca = s[2]
        descricao = s[3]
        precocom = s[4]
        precoven = s[5]
        quantidade = s[6]

        novoProduto = Produto(id, nome, marca, descricao, precocom, precoven, quantidade)
        lista_produtos.append(novoProduto)"""

    conn.close()
    return lista_produtos

def getProduto(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """SELECT * FROM produtos where id= ?;"""        
    cursor.execute(sql, [id])
    s = cursor.fetchall()[0]
     
    id = s[0]
    nome = s[1]
    marca = s[2]
    descricao = s[3]
    precocom = s[4]
    precoven = s[5]
    quantidade = s[6]
    #cria novo objeto
    novoProduto = Produto(id, nome, marca, descricao, precocom, precoven, quantidade)
    # fecha a conexão
    conn.close()  
    return novoProduto

def addPoduto(produto):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """INSERT INTO Produtos (nome,marca,descricao,precocom,precoven, quantidade)
               VALEUS (?, ?, ?, ?,?):"""
    cursor.execute(sql,[produto.nome, produto.marca, produto.descricao, produto.precocom, produto.precoven, produto.quantidade])
    conn.commit()
    conn.close()  

def editProduto(produto):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """UPDATE produtos SET nome = ?, marca = ?, descricao = ?, precocom = ?, precoven = ?, quantidade = ? WHERE id = ?"""
    cursor.execute(sql,[produto.nome, produto.marca, produto.descricao, produto.precocom, produto.precoven, produto.quantidade])
    conn.commit()
    conn.close()

def delProduto(id):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql = """ DELETE FROM produtos WHERE id = ?"""
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()    

