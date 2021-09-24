from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize, QRect


class TabelaItens():
    def __init__(self, tableWidget, parent):
        # ATRIBUTO DA CLASSE
        self.tableWidget = tableWidget
        self.parent = parent

        self.itemAtual = None
        self.listaItens = []

        # Configuração da tabela
        self.configTable()

        self.tableWidget.setRowCount(0)

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.tableWidget.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        # ajusta as colunas ao tamanho da tela
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1,
                                                                 QHeaderView.Stretch)

        # desabilita a edição dos campos

        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.tableWidget.clicked.connect(self.on_click)

    def on_click(self):
        # linha onde foi clicado
        selected_row = self.tableWidget.currentRow()
        self.itemAtual = self.listaItens[selected_row]
        self.parent.p_remover.setEnabled(True)

    def _addRow(self, item):
        self.listaItens.append(item)
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        qtd = QTableWidgetItem(str(item.quantidade))
        nome_produto = QTableWidgetItem(item.getNomeProduto())
        uni = QTableWidgetItem(str(item.getValorUnitario()))
        valor = QTableWidgetItem(str(item.getValor()))
        # insere os itens na tabela
        self.tableWidget.setItem(rowCount, 0, qtd)
        self.tableWidget.setItem(rowCount, 1, nome_produto)
        self.tableWidget.setItem(rowCount, 2, uni)
        self.tableWidget.setItem(rowCount, 3, valor)
        
        self.tableWidget.setCellWidget(rowCount, 4, CustomQWidget(item,self))
        self.calculaValorTotal()

    def calculaValorTotal(self):
        valorTotal = 0
        desconto = self.parent.desconto.text()
        if desconto == "":
            desconto = "0"

        for item in self.listaItens:
            valorTotal += (float(item.getValor()))

        desconto = float(desconto)  
        if desconto < valorTotal:
            valorTotal = valorTotal - desconto  

        self.parent.valor_total.setText("%.2f" % valorTotal)      
    
    def limparItens(self):
        self.tableWidget.setRowCount(0)
        self.itemAtual = None
        self.listaItens = []
        #desativo os botões
        self.parent.p_remover.setEnabled(False)
        self.parent.p_limpar.setEnabled(False)
            
        self.parent.carregaDadosProdutos()   
        self.calculaValorTotal() 
    
    def limparSelecionado(self):
        self.listaItens.remove(self.itemAtual)
        novaLista = self.listaItens

        self.limparItens()
        self.parent.p_limpar.setEnabled(True)
        
        for p in novaLista:
            self._addRow(p)

class CustomQWidget(QWidget):
    def __init__(self, item, parent):
        super(CustomQWidget, self).__init__()
        self.item = item
        self.parent = parent
        self.btn = QPushButton(self)
        self.btn.setText("")          
        self.btn.setIcon(QIcon("icons/delete.png"))  
        self.btn.setShortcut('Ctrl+D')  
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip("Remover item "+str(self.item.produto.nome)+"?") 
        self.btn.setStyleSheet('QPushButton {background-color: #00FFFFFF; border:  none}')
        self.btn.setIconSize(QSize(20,20))
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def remover(self):
        self.parent.itemAtual = self.item
        self.parent.limparSelecionado()
        print("Remover item: ", self.item.produto.nome)