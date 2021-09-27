
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.clientes_model as CliModel


class TabelaClientes(QTableWidget):
    def __init__(self, janela_pai):
        super().__init__(0, 6)
        self.janela_pai = janela_pai

        headers = ["ID", "Nome", "CPF", "TELEFONE", "EMAIL", "ENDERECO"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()
        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)

        self.horizontalHeader().setStretchLastSection(False) 
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)

        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)
       # self.clicked.connect(self.on_click)
    
    def carregaDados(self):
        self.lista_clientes = CliModel.getClientes() 
        self.setRowCount(0) 
        for clientes in self.lista_clientes:
            self.addRow(clientes)

    def addRow(self, clientes):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        id = QTableWidgetItem(str(clientes.id))
        nome = QTableWidgetItem(clientes.nome)
        cpf = QTableWidgetItem(clientes.cpf)
        telefone = QTableWidgetItem(clientes.telefone)
        email = QTableWidgetItem(clientes.email)
        endereco = QTableWidgetItem(clientes.endereco)
    
        self.setItem(rowCount, 0, id)
        self.setItem(rowCount, 1, nome)
        self.setItem(rowCount, 2, cpf)
        self.setItem(rowCount, 3, telefone) 
        self.setItem(rowCount, 4, email) 
        self.setItem(rowCount, 5, endereco)        

    def on_click(self):
        selected_row = self.current_Row()
        id = self.item(selected_row, 0).text()   
        cliente = CliModel.getClientes(id)
        self.janela_pai.insereInfo(cliente)

    def add(self, cliente):
        CliModel.addCliente(cliente)
        self.carregaDados()

    def update(self, cliente):
        CliModel.editCliente(cliente)
        self.carregaDados()

    def delete(self, cliente):
        CliModel.delCliente(cliente.id)
        self.carregaDados()            
    