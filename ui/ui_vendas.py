from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidget
from PyQt5 import uic

import models.vendas_model as VenModel

class Vendas(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_vendas.ui", self)

        #self.configTable()

        #self.lista_de_vendas = []
        #self.carregaVendas()

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3,
                                                                 QHeaderView.Stretch)

        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(False)        
    
    def carregaVendas(self):
        self.lista_de_vendas = VenModel.getVendas()
        print(len(self.lista_de_vendas))
        