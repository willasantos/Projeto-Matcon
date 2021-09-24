import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QListWidgetItem
from PyQt5 import uic

from ui.ui_produtos import CadProdutos
from ui.ui_clientes import CadClientes
from ui.ui_vendas import Vendas
from ui.ui_novavenda import NovaVenda

from qt_material import apply_stylesheet

class CustomQWidget(QWidget):
    def __init__(self, icon, text, parent=None):
        super(CustomQWidget, self).__init__(parent)

        label_icon = QLabel(icon)
        label_text = QLabel(text)

        layout = QHBoxLayout()
        layout.addWidget(label_icon)
        layout.addWidget(label_text)
        layout.addWidget(label_icon)

        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "PRODUTOS")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(0,item)
        self.listWidget.setItemWidget(item, item_widget)

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "CLIENTES")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(1,item)
        self.listWidget.setItemWidget(item, item_widget)
        
        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "NOVA VENDA")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(1,item)
        self.listWidget.setItemWidget(item, item_widget) 

        item = QListWidgetItem(self.listWidget)
        item_widget = CustomQWidget("+", "LISTA DE VENDAS")
        item.setSizeHint(item_widget.sizeHint())
        self.listWidget.insertItem(1, item)
        self.listWidget.setItemWidget(item, item_widget)
        
        self.listWidget.setCurrentRow(0)
        self.carregaJanelas()
        self.listWidget.currentRowChanged.connect(self.display)

    def carregaJanelas(self):
        self.stackedWidget.insertWidget(0, CadProdutos())
        self.stackedWidget.insertWidget(1, CadClientes())
        self.stackedWidget.insertWidget(2, NovaVenda())
        self.stackedWidget.insertWidget(3, Vendas())

    def display(self, index):
        self.carregaJanelas()
        self.stackedWidget.setCurrentIndex(index)
        self.listWidget.setCurrentRow(index)


app = QApplication(sys.argv)
apply_stylesheet(app, theme='dark_pink.xml')

window = MainWindow()
window.show()

app.exec()