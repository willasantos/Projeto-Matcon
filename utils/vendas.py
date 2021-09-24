
class Venda():
    def __init__(self, id, cliente, lista_itens, valor_total, data):
        self.id = -1
        self.cliente = cliente
        self.lista_itens = lista_itens
        self.valor_total = valor_total
        self.data = data

    def qtdItens(self):
        return len(self.lista_itens)   

    def getItens(self):
        return self.lista_itens

    def getValorTotal(self):
        return self.valor_total            
        

    