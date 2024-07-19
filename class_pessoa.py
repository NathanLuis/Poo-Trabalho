class Pessoa:

    def __init__(self, nome, telefone, idade, genero, endereco):
        self.__nome = nome
        self.__telefone = telefone
        self.__idade = idade
        self.__genero = genero
        self.__endereco = endereco

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _telefone(self):
        return self.__telefone

    @_telefone.setter
    def _telefone(self, value):
        self.__telefone = value
    
    @property
    def _idade(self):
        return self.__idade
    
    @_idade.setter
    def _idade(self, value):
        self.__idade = value
    
    @property
    def _genero(self):
        return self.__genero
    
    @_genero.setter
    def _genero(self, value):
        self.__genero = value
    
    @property
    def _endereco(self):
        return self.__endereco
    
    @_endereco.setter
    def _endereco(self, value):
        self.__endereco = value

