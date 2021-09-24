from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp, QDate
from PyQt5 import uic

import models.clientes_model as CliModel
import models.produtos_model as ProdModel
import models.vendas_model as VenModel
from ui.table_itensven import TabelaItens
from utils.item_venda import ItemVenda
from utils.vendas import Venda

class NovaVenda(QWidget):
    def __init__(self):
        super(). __init__()
        uic.loadUi("ui/ui_novavenda.ui", self)

        self.clienteAtual = None
        self.produtoAtual = None
        self.lista_clientes = []
        self.lista_produtos = []

        self.carregaDadosClientes()
        self.carregaDadosProdutos()

        self.setEventos()

        self.tabelaItens = TabelaItens(self.tableWidget, self)

        qtd_validator = QRegExpValidator(QRegExp('^[1-9]{1}[0-9]{5}$'), self.quantidade_2)
        self.quantidade_2.setValidator(qtd_validator)

        desconto_validator = QRegExpValidator(
            QRegExp('^[0-9]+(\.[0-9]{1,2})?$'), self.desc_line)
        self.desc_line.setValidator(desconto_validator)

        self.dateEdit.setDate(QDate.currentDate())

    def carregaDadosClientes(self):
        self.lista_clientes = CliModel.getClientes()
        lista_combo = []
        for c in self.lista_clientes:
            lista_combo.append(c.nome)
        self.combo_clientes.addItems(lista_combo)
    
    def carregaDadosProdutos(self): 
        self.combo_produtos.clear()
        self.lista_produtos = ProdModel.getProdutos()
        lista_combo = []
        for p in self.lista_produtos:
            lista_combo.append(p.nome)
        self.combo_produtos.addItems(lista_combo)

    def setEventos(self):
        self.combo_clientes.currentIndexChanged.connect(
            self.index_changed_cliente)
        self.combo_produtos.currentIndexChanged.connect(
            self.index_changed_produto)

        self.adc_item.clicked.connect(self.addItem)

        self.p_limpar.clicked.connect(self.limparItens)

        self.p_remover.clicked.connect(self.limparSelecionado)

        self.quant_disp.textEdited.connect(self.qtd_edited)

        self.desc_line.textEdited.connect(self.atualizaValorTotal)

        self.bt_finalizar.clicked.connect(self.finalizaVenda)

       # self.combo_pag.currentIndexChanged.connect(self.atualizaValorTotal)

    def atualizaValorTotal(self):
        self.tabelaItens.calculaValorTotal()    

    def index_changed_cliente(self, i):  
        self.clienteAtual = self.lista_clientes[i]
        self.id_line.setText(str(self.lista_clientes[i].id))   

    def index_changed_produto(self, i):  
        self.produtoAtual = self.lista_produtos[i]
        self.marca_line.setText(self.lista_produtos[i].marca)
        self.valor_line.setText(str(self.lista_produtos[i].precoven))
        self.quant_disp.setText(str(self.lista_produtos[i].quantidade))
        self.desc.setText(self.lista_produtos[i].descricao)     
   
    def addItem(self):
        item = ItemVenda(self.quantidade_2.text(), self.produtoAtual)
        self.tabelaItens._addRow(item)
        self.b_limpar.setEnabled(True)
        self.adc_item.setEnabled(False)
        self.quant_disp.setText("")

        index = self.lista_produtos.index(self.produtoAtual)
        p = self.lista_produtos[index]
        p.quantidade = item.novaQtd()

        self.atualizaListaProdutos()

    def atualizaListaProdutos(self):
        self.combo_produtos.clear()  
        lista_combo = []
        for p in self.lista_produtos:
            lista_combo.append(p.nome)
        self.combo_produtos.addItems(lista_combo)    
     
    def limparItens(self):
        self.tabelaItens.limparItens()

    def limparSelecionado(self):
        self.tabelaItens.limparSelecionado()

    def qtd_edited(self, s):
        if s!="" and int(s) <= self.produtoAtual.quantidade:
            self.adc_item.setEnabled(True)
        else:
            self.adc_item.setEnabled(False) 

    def finalizaVenda(self):
        data = self.dateEdit.dateTime().toString('dd/MM/yyyy')
        cliente = self.clienteAtual
        lista_de_itens = self.tabelaItens.listaItens
        valor_total = self.valor_total.text()
        novaVenda = Venda(-1, cliente, lista_de_itens, valor_total, data)
        VenModel.addVenda(novaVenda)   

        self.limparItens()        