from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
import models.produtos_model as ProdModel

class TabelaProdutos(QTableWidget):
    def __init__(self, janela_pai):
        super().__init__(0, 7) 

        self.janela_pai = janela_pai

        headers = ["ID", "NOME","MARCA", "DESCRICAO","PRECOCOM", "PRECOVEN", "QUANTIDADE"]  
        self.setHorizontalHeaderLabels(headers)

        self.configTable()

        self.lista_produtos = []

        self.carregaDados()
  
    def configTable(self):
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        
        self.setEditTriggers(QTableWidget.NoEditTriggers)
       
        self.setSelectionBehavior(QTableWidget.SelectRows)
        
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_produtos = ProdModel.getProdutos()
        self.setRowCount(0)
        for produtos in self.lista_produtos:
            self.addRow(produtos)

    def addRow(self, produtos):
        rowCount = self.rowCount()
        self.insertRow(rowCount)

        id = QTableWidgetItem(str(produtos.id))   
        nome = QTableWidgetItem(produtos.nome)  
        marca = QTableWidgetItem(produtos.marca)
        descricao = QTableWidgetItem(produtos.descricao)
        precocom = QTableWidgetItem(str(produtos.precocom)) 
        precoven = QTableWidgetItem(str(produtos.precoven)) 
        quantidade  = QTableWidgetItem(str(produtos.quantidade))

        self.setItem(rowCount, 0, id)
        self.setItem(rowCount, 1, nome)
        self.setItem(rowCount, 2, marca)
        self.setItem(rowCount, 3, descricao)
        self.setItem(rowCount, 4, precocom)
        self.setItem(rowCount, 5, precoven) 
        self.setItem(rowCount, 6, quantidade)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        produto = ProdModel.getProduto(id)
        self.janela_pai.insereInfo(produto)

    def add(self, produto):
        ProdModel.addProduto(produto)
        self.carregaDados()

    def update(self, produto):
        ProdModel.editProduto(produto)
        self.carregaDados()

    def delete(self, produto):
        ProdModel.delProduto(produto.id)
        self.carregaDados()        


    