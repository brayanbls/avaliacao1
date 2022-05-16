class Ferramenta:
    def __init__(self, nome, tensao, preco):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco

    def getInformacoes(self):
        print("Nome: ",self.nome)
        print("Tensao: ", self.tensao)
        print("Preco: ", self.preco)

    def cadastrar(self,nome, tensao, preco):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco
        print('Novo nome cadastrado:',self.nome)
        print('Nova tensao cadastrada:', self.tensao)
        print('Novo preço cadastrado:', self.preco)

class Furadeira(Ferramenta):
    def __init__(self,nome,tensao,preco,potencia):
        super().__init__(nome,tensao,preco)
        self._potencia = potencia

    def getInformacoes(self):
        super().getInformacoes()
        print('Potencia: ',self._potencia)

class Lixadeira(Ferramenta):
    def __init__(self,nome,tensao,preco,rotacao):
        super().__init__(nome,tensao,preco)
        self.__rotacao = rotacao

    def getInformacoes(self):
        super().getInformacoes()
        print('Potencia: ',self.__rotacao)