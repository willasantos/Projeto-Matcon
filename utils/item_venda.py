class ItemVenda:
    def __init__(self,quantidade, produto, valor_uni):
        self.quantidade = quantidade
        self.produto = produto
        self.valor_uni = valor_uni
    
    def getNomeProduto(self):
        return self.produto.nome
    
    def getValorUnitario(self):
        return self.produto.precoven
    
    def getValor(self):
        return "%.2f" % (float(self.produto.precoven) * float(self.quantidade))

    def novaQtd(self):
        return int("%.0f" % (int(self.produto.quantidade) - int(self.quantidade)))    