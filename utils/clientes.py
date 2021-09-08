## classe cliente
## atributos do clientes = aos campos da tabela cliente

class Cliente:
    def __int__(self, id, nome, cpf, telefone, email, endereco):
     self.id = id
     self.nome = nome
     self.cpf = cpf
     self.telefone = telefone
     self.email = email
     self.endereco = endereco 

    def print(self):
        info = [self.id, self.nome, self.cpf, self.telefone, self.email, self.endereco]
        print(info)

    def getinfo(self):
        info = [self.id, self.nome]
        return info    
