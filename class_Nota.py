import datetime


class Nota:

    def __init__(self, pedido, cliente, atendente, ):
        self.__pedido = pedido
        self.__cliente = cliente
        self.__atendente = atendente
        self.__horaGerada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for iterado in pedido.itens_pedidos:
            self.__valorTotal += iterado.produto.preco * iterado.quantidade
        self._valorTotal = self.calcular_valor_total()


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

def calcular_valor_total(self):
        valor_total = 0.0
        for item in self._pedido._itens_pedidos:
            valor_total += item._preco_item
        return valor_total


    def toString(self):
        info_nota = "NOTA FISCAL"
        info_nota += f"Pedido: {self._pedido._codigo_pedido}\n"
        info_nota += f"Cliente: {self._cliente._nome}\n"
        info_nota += f"Atendente: {self._atendente._nome}\n"
        info_nota += f"Data/Hora: {self._horaGerada}\n"
        info_nota += f"Valor Total: R$ {self._valorTotal:.2f}\n"
        info_nota = "FIM DA NOTA FISCAL" 
        return info_nota

# Observar a funcinalidade da função calcular valor total e o toSting se está implementao corretamente
