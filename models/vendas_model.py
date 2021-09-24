from utils.vendas import Venda
from utils.item_venda import ItemVenda

import  models.database as db
import models.produtos_model as ProdModel
import models.clientes_model as CliModel

def addVenda(venda):
    conn = db.connect_db()
    cursor = conn.cursor()
    sql_addVenda = """INSERT INTO vendas (id_cliente, valor_total, data)
               VALEUS (?,?,?):"""
    valuesVenda = [venda.cliente.id, venda.getValorTotal(), venda.data]
    cursor.execute(sql_addVenda, valuesVenda)   
    conn.commit()        

    sql_id_venda = "SELECT LAST_INSERT_ROWID() AS id;" 
    cursor.execute(sql_id_venda)
    rowID = cursor.fetchall()[0]
    id_venda = rowID[0]
     
    sql_addItens = "INSERT INTO itemVenda (id_venda, id_produtos, quant, valor_uni) VALUES (?,?,?):" 

    listaItens = venda.getItens() 
    for item in listaItens:
        valuesItem = [id_venda, item.produto.id, item.quantidade, item.getValorUnitario()]
        cursor.execute(sql_addItens, valuesItem)
        conn.commit()
    conn.close

def getVendas():
    conn = db.connect_db()
    cursor = conn.cursor()
    lista_de_vendas = []
    sql = "SELECT * FROM vendas; "
    cursor.execute(sql)
    for v in cursor.fetchall(): # para cada venda faz:
        id_venda = v[0]
        id_cliente = v[1]
        valor_total = v[2]
        data = v[3]     

        lista_itens = []
        sql_itens = "SELECT * FROM ItensVenda WHERE id_venda = ?;"
        valuesItens = [id_venda]
        cursor.execute(sql_itens, valuesItens)
        for i in cursor.fetchall():
            id_produto = i[1]
            quant = i[2]
            valor_uni = i[3]

            produto = ProdModel.getProduto(id_produto)  
            item = ItemVenda(quant, produto, valor_uni)
            lista_itens.append(item)

        cliente = CliModel.getCliente(id_cliente)
        venda = Venda(id_venda, cliente, lista_itens, valor_total, data)
        lista_de_vendas.append(venda)
    conn.close()
    return lista_de_vendas
    



