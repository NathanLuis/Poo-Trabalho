class Pedido:

    def __init__(self, codigoDoPedido, cliente, atendente, valorTotal, horaGerada):
        self.__codigoDoPedido = codigoDoPedido
        self.__cliente = cliente
        self.__atendente = atendente
        self.__valorTotal = valorTotal
        self.__horaGerada = horaGerada
    

    @property
    def _codigoDoPedido(self):
        return self.__codigoDoPedido

    @_codigoDoPedido.setter
    def _codigoDoPedido(self, value):
        self.__codigoDoPedido = value

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