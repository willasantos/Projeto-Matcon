
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
import models.produtos_model as ProdModel

class TabelaProdutos(QTableWidget):
    def __init__(self, janela_pai):
        super().__init__(0, 7) # config inicial da tabela(qtd_linha, qtd_colunas)

        # possui a referencia do pai
        self.janela_pai = janela_pai

        # textos do cabeçalho
        headers = ["ID", "NOME","MARCA", "DESCRICAO","PRECOCOM", "PRECOVEN", "QUANTIDADE"]  #alterar aqui
        self.setHorizontalHeaderLabels(headers)

        #Configuração da tabela
        self.configTable()

       
    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
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


    