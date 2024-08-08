# definição da classe
class Pedido:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor
    def __init__(self, codido_pedido, endereco_entrega):
        self.__codigo_pedido = codido_pedido
        self.__endereco_entrega = endereco_entrega
        self.__status = 0  # 0 = aberto, 1 = finalizado/pago
        # criando uma estrutura map em python para armzenar itens do pedido
        self.__itens_pedidos = []

    @property
    def _status(self):
        return self.__status

    @_status.setter
    def _status(self, value):
        self.__status = value

    @property
    def _codigo_pedido(self):
        return self.__codigo_pedido

    @_codigo_pedido.setter
    def _codigo_pedido(self, value):
        self.__codigo_pedido = value

    @property
    def _endereco_entrega(self):
        return self.__endereco_entrega

    @_endereco_entrega.setter
    def _endereco_entrega(self, value):
        self.__endereco_entrega = value

    @property
    def _itens_pedidos(self):
        return self.__itens_pedidos

    @_itens_pedidos.setter
    def _itens_pedidos(self, value):
        self.__itens_pedidos = value

    def adicionar_item_ao_pedido(self, itempedido):
        item_found = False
        for item in self.__itens_pedidos:
            if item._produto._codigo_produto == itempedido._produto._codigo_produto:
                item._quantidade += itempedido._quantidade
                item._preco_item = item._produto._preco * item._quantidade
                item_found = True
                print("Pedido atualizado com sucesso!")
                break  # Exit the loop once the item is found and updated
        if not item_found:
            self.__itens_pedidos.append(itempedido)
            print("Item adicionado ao pedido com sucesso!")

    def remover_item_pedido(self, itempedido):
        self.__itens_pedidos.pop(itempedido)

    def quantidade_itens_pedido(self):
        return int(len(self.__itens_pedidos))
        # return self.__itens_pedidos.__sizeof__

    def toString(self):
        str_line = "** INÍCIO DAS INFORMAÇÕES DO PEDIDO **"
        print(str_line, end='\n')
        str_line = "CÓDIGO DO PEDIDO:" + str(self._codigo_pedido)
        print(str_line, end='\t')
        str_line = "STATUS DO PEDIDO:" + \
            str(self._status)  # (0-aberto | 1-finalizado)
        print(str_line, end='\n')
        str_line = "CEP ENDEREÇO PARA ENTREGA:" + \
            str(self._endereco_entrega._cep)
        print(str_line, end='\t')
        str_line = "RUA:" + str(self._endereco_entrega._rua)
        print(str_line, end='\t')
        str_line = "BAIRRO/CIDADE PARA ENTREGA:" + \
            str(self._endereco_entrega._bairro) + "/" + \
            str(self._endereco_entrega._cidade)
        print(str_line, end='\n')
        str_line = "QUANTIDADE DE ITENS DO PEDIDO:" + \
            str(self.quantidade_itens_pedido())
        print(str_line, end='\n')
        dbl_preco_total = 0.0
        for i, item in enumerate(self._itens_pedidos):
            str_line = "\t #ITEM:" + str(i)
            print(str_line, end='\t')
            str_line = "PRODUTO:" + str(item._produto._descricao)
            print(str_line, end='\t')
            str_line = "QTD (#):" + str(item._quantidade)
            print(str_line, end='\t')
            str_line = "SUBTOTAL (R$):" + str(item._preco_item)
            dbl_preco_total += item._preco_item
            print(str_line, end='\n')
        str_line = "PREÇO TOTAL DO PEDIDO:" + str(dbl_preco_total)
        print(str_line, end='\n')
        str_line = "** FIM DAS INFORMAÇÕES DO PEDIDO **"
        print(str_line, end='\n')
