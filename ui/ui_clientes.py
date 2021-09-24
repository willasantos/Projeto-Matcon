from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from utils.clientes import Cliente
from ui.table_clientes import TabelaClientes

class CadClientes(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_clientes.ui", self)

        #insere a tabela no layout
        self.table = TabelaClientes(self)
        
        # insere a table no layout do main_window
        self.verticalLayout.addWidget(self.table)

        self.clienteAtual = None
        self.setEventos()

    def setEventos(self):
        self.b_salvar.clicked.connect(self.salvarCliente)
        self.b_limpar.clicked.connect(self.limpaCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def salvarCliente(self):
        # adiciona os campos na tabela
        novo = self.getCliente()

        if novo != None:
           
            if self.clienteAtual == None:
                
                self.table.add(novo)
            else:
                novo.id = self.clienteAtual.id
                self.table.update(novo)
           
            self.limpaCampos()    

    def getCliente(self):
        nome = self.nome.text()
        cpf = self.cpf.text()
        telefone = self.fone.text()
        email = self.email.text()
        endereco = self.endereco.text()

        if((nome != "") and (cpf != "") and (telefone != "") and (email != "") and (endereco != "")):
            return Cliente(-1, nome, cpf, telefone, email, endereco)
        return None      

    def limpaCampos(self):
        self.clienteAtual = None
        self.nome.setText("")
        self.cpf.setText("")
        self.telefone.setText("")
        self.email.setText("")
        self.endereco.setText("")

        self.b_salvar.setText("Salvar")
        self.b_excluir.setEnabled(False)

    def insereInfo(self, cliente):
        self.clienteAtual = cliente
        self.nome.setText(cliente.nome)
        self.cpf.setText(cliente.cpf)
        self.telefone.setText(cliente.telefone)
        self.email.setText(cliente.email)
        self.endereco.setText(cliente.endereco)

        self.b_salvar.setText("Atualizar")
        self.b_excluir.setEnabled(True)    

    def excluirItem(self):
        self.table.delete(self.clienteAtual)
        self.limpaCampos()    
          