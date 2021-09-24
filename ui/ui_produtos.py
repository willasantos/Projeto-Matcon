from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from ui.table_produtos import TabelaProdutos
from utils.produtos import Produto


class CadProdutos(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_produtos.ui", self) 

        self.table = TabelaProdutos(self)
        
        self.verticalLayout.addWidget(self.table)

        self.produtoAtual = None

        self.setEventos()

    def setEventos(self):
        self.b_salvar.clicked.connect(self.salvar)
        self.b_limpar.clicked.connect(self.limpaCampos)
        self.b_excluir.clicked.connect(self.excluir)   

    def salvar(self):
        # adiciona os campos na tabela
        novo = self.getProduto()
        # verifica os campos vazios
        if novo != None:
            # é um novo contato
            if self.produtoAtual == None:

                self.table.add(novo)
            else:
                # manda editar no bando de dados
                novo.id = self.produtoAtual.id
                self.table.update(novo)
           
            self.limpaCampos()

    def getProduto(self):
        nome = self.nome.text()
        marca = self.marca.text()
        descricao = self.descricao.text()
        precocom = self.preco_compra.text()
        precoven = self.preco_venda.text()
        quantidade = self.quantidade.text()

        if((nome != "") and (marca != "") and (descricao != "") and (precocom != "") and (precoven != "") and (quantidade != "")):
            return Produto(id, nome, marca, descricao, precocom, precoven, quantidade)
        return None  

    def limpaCampos(self):
        self.produtoAtual = None
        self.nome.setText("")
        self.marca.setText("")
        self.descricao.setText("")
        self.precocom.setText("")
        self.precoven.setText("")
        self.quantidade.setText("")

        self.b_salvar.setText("Novo")
        self.b_excluir.setEnabled(False)          

    def insereInfo(self, produto):
        self.produtoAtual = produto
        self.nome.setText(produto.nome)
        self.marca.setText(produto.marca)
        self.descricao.setText(produto.descricao)
        self.precocom.setText(str(produto.precocom))
        self.precoven.setText(str(produto.precoven))
        self.quantidade.setText(str(produto.quantidade))

        self.b_salvar.setText("Atualizar")
        self.b_excluir.setEnabled(True)

    def excluir(self):
        self.table.delete(self.produtoAtual)
        self.limpaCampos()