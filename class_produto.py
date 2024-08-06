# definição da classe
class Produto:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor 
    def __init__(self, codigo_produto, descricao, preco, validade):
        self.__codigo_produto = codigo_produto # __ modificador de acesso private
        self.__descricao = descricao
        self.__preco = preco
        self.__validade = validade

    @property
    def _codigo_produto(self):
        return self.__codigo_produto

    @_codigo_produto.setter
    def _codigo_produto(self, value):
        self.__codigo_produto = value

    @property
    def _descricao(self):
        return self.__descricao

    @_descricao.setter
    def _descricao(self, value):
        self.__descricao = value

    @property
    def _preco(self):
        return self.__preco

    @_preco.setter
    def _preco(self, value):
        self.__preco = value

    @property
    def _validade(self):
        return self.__validade

    @_validade.setter
    def _validade(self, value):
        self.__validade = value

    def toStringForSaveLoadMethod(self):
        return str(f'{self.__codigo_produto},{self.__descricao},{self.__preco},{self.__validade}')
    
    def fromStringToSaveLoadMethod(String):
        attributes = String.strip().split(',')
        if len(attributes) == 4:
            codigo_produto = attributes[0]
            descricao = attributes[1]
            preco = float(attributes[2])
            validade = attributes[3]
            return Produto(codigo_produto,descricao,preco,validade)
        else:
            print(f"Erro: Linha malformada encontrada: {String.strip()}")
            return None