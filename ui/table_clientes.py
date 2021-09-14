
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.clientes_model as CliModel


class TabelaClientes(QTableWidget):
    def __init__(self, janela_pai):
        super().__init__(0, 6)
        self.janela_pai = janela_pai

        headers = ["ID", "Nome", "CPF", "TELEFONE", "EMAIL", "ENDERECO"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()


    def configTable(self):
        self.verticalHeader().setVisible(False)

        self.horizontalHeader().setStretchLastSection(False) 
        self.horizontalHeader().setSectionResizeMode( QHeaderView.Stretch)

        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)
       # self.clicked.connect(self.on_click)

    def on_click(self):
        #linha onde foi clicado
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
    