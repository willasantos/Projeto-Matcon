
class Produto:
    def __int__(self,id, nome, marca, descricao, precocom, precoven, quantidade):
     self.id = id
     self.nome = nome
     self.marca = marca
     self.descricao = descricao
     self.precocom = precocom
     self.precoven = precoven
     self.quantidade = quantidade

    def imprimir(self):
        info = [self.id, self.nome, self.marca, self.descricao, self.precocom, self.precoven, self.quantidade]
        print(info)

    def printInfo(self):
        info = [self.id, self.nome, self.precoven] 
        print(info)   
         