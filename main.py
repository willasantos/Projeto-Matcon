import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

from ui.ui_produtos import Cadprodutos
from ui.ui_clientes import Cadclientes

class MainWindow(QMainWindow):
    def __int__(self):
        super().__init__()
        uic.loadUi("mainwindow.ui", self)
        self.b_cadProdutos.clicked.connect(self.openCadProdutos)
        self.b_cadClientes.clicked.connect(self.openCadClientes)

    def openCadProdutos(self):
       self.w = Cadprodutos()
       print("clique em produtos")
       self.w.show()

    def openCadClientes(self):
        self.w = Cadclientes()
        print("clique em clientes")
        self.w.show()    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()