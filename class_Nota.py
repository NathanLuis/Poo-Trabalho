import datetime


class Nota:

    def __init__(self, pedido, cliente, atendente, ):
        self.__pedido = pedido
        self.__cliente = cliente
        self.__atendente = atendente
        self.__horaGerada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for iterado in pedido.itens_pedidos:
            self.__valorTotal += iterado.produto.preco * iterado.quantidade


    @property
    def _pedido(self):
        return self.__pedido

    @_codigoDoPedido.setter
    def _pedido(self, value):
        self.__pedido = value

    @property
    def _cliente(self):
        return self.__cliente
    
    @_cliente.setter
    def _cliente(self, value):
        self.__cliente = value
    
    @property
    def _atendente(self):
        return self.__atendente
    
    @_atendente.setter
    def _atendente(self, value):
        self.__atendente = value
    
    @property
    def _valorTotal(self):
        return self.__valorTotal
    
    @_valorTotal.setter
    def _valortotal(self, value):
        self.__valorTotal = value
    
    @property
    def _horaGerada(self):
        return self.__horaGerada
    
    @_horaGerada.setter
    def _horaGerada(self, value):
        self.__horaGerada = value

    # def toString(self):       a implementar
