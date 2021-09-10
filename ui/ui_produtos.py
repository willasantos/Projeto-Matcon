from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class Cadprodutos(QWidget):
    def __int__(self):
        super().__init__()
        uic.loadUi("ui/ui_produtos.ui", self) 

        self.b_salvar.clicked.connect(self.salvarVenda)

    def salvarVenda(self):
        nome = self.nome.text()
        marca = self.marca.text()
        descricao = self.descricao.text()
        precocom = self.precocom.text()
        precoven = self.precoven.text()
        quantidade = self.quantidade.text()

        print("Venda adicionada!")
        self.inform.setText("Esta venda foi adicionada com sucesso!!")    
        self.limparCampos()

    def limparCampos(self):
        self.nome.setText("")
        self.marca.setText("")
        self.descricao.setText("")
        self.precocom.setText("")
        self.precoven.setText("")  
        self.quantidade.setText("")  


