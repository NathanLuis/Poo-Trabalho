from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_pessoa import Pessoa
from class_produto import Produto
from class_nota import nota

from datetime import datetime


def menu_principal():  # MENU PRINCIPAL
    print('''
        MENU Principal:
        [1] - Controle de vendas
        [2] - Cadastrar novo produto
        [3] - Remover um produto
        [4] - Pesquisar um produto
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))


def menu_pedido():
    print('''
        MENU Vendas:
        [1] - Abrir novo pedido
        [2] - Adicionar item ao pedido
        [3] - Remover item do pedido
        [4] - Listar itens do pedido em detalhes
        [5] - Finalizar pedido e imprimir
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))


def pedido_adicionar():
    # código pedido gerado automaticamente
    endereco_pedido = cadastrar_endereco()
    # a numeração do pedido começa de 1 até n
    codido_pedido = int(len(pedidos)) + 1
    return Pedido(codido_pedido, endereco_pedido)
def exibe_pedidos_em_aberto():
    count = 1
    for iterado in pedidos:
        if iterado.status == 0:
            print('Aberto Nº ' + str(count))
            print(iterado.toString())
            count += 1


def finalizar_pedido():
    exibe_pedidos_em_aberto();
    selecao = int(input('Insira o CODIGO do Pedido a finalizar \n O pedido que está prestes a finalizar não poderá ser modificado.'))

    pedido_atual = buscar_pedido_por_codigo(selecao)
    pedido_atual.status = 1
    print('Pedido finalizado com sucesso! \n Agora insira os dados do cliente e funcionário.')
    cliente_atual = cadastrar_cliente()
    funcionario_atual = cadastrar_funcionario()
    nota_atual = nota(pedido_atual, cliente_atual, funcionario_atual)
    print('Nota gerada com sucesso! \n' + nota_atual)
    historico_notas.append(nota_atual)

#def gera_nota_fiscal():

#def exibe_notas():
def pedido_adicionar_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para adicionar um novo item: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_produto = int(input('Informe o código do produto para adicionar ao pedido: '))
        produto = buscar_produto_por_codigo(int_codigo_produto)
        if produto:
            int_quantidade_item = int(input('Informe a quantidade do item:'))
            novo_item_pedido = ItemPedido(produto, int_quantidade_item)
            pedido.adicionar_item_ao_pedido(novo_item_pedido)
        else:
            print("Não foi possível adicionar este produto, pois o código do produto não existe!")
        # return Pedido(codido_pedido, endereco_pedido)
    else:
        print("Pedido inexistente")
        return False


def pedido_remover_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para remover um item selecionado: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_item = int(
            input('Informe o número do item para remover deste pedido ' + str(pedido._codigo_pedido) + ': '))
        # verifica se número intem informado existe: não faz sentido remover item 5 se ele não existe
        # if pedido.quantidade_itens_pedido() <= int_codigo_item:
        pedido.remover_item_pedido(int_codigo_item)
    else:
        print("Pedido inexistente")
        return False


def pedido_listar_items():
    int_pedido_selecionado = int(input('Informe o código do pedido para mais detalhes: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        pedido.toString()
    else:
        print("Pedido inexistente")
        return False


def cadastrar_endereco():
    str_cep = str(input('Informe o cep do endereço: '))
    str_rua = str(input('Informe a rua: '))
    int_num = int(input('Informe o número: '))
    str_complemento = str(input('Informe o complemento do endereço: '))
    str_bairro = str(input('Informe o bairro: '))
    str_cidade = str(input('Informe a cidade: '))
    endereco = Endereco(str_cep, str_rua, int_num,
                        str_complemento, str_bairro, str_cidade)
    return endereco


def cadastrar_produto():
    int_codigo = int(input('Informe o código identificador do produto: '))
    str_nome = str(input('Qual o nome/descrição do produto? '))
    flt_preco = float(input('Informe o valor (ex. 0.00): '))
    date_validade = (input('Informe a validade do produto (formato dd/mm/aaaa): '))
    date_validade = datetime.strptime(date_validade, '%d/%m/%Y')
    return Produto(int_codigo, str_nome, flt_preco, date_validade)


def remover_produto():
    int_codigo_remocao = int(input('Informe o código do produto para remoção: '))
    produto_remover = estoque_produtos[int_codigo_remocao]
    print("Produto (" + produto_remover._descricao + ") removido!")
    del estoque_produtos[int_codigo_remocao]


def buscar_produto_por_codigo(int_codigo_produto):
    # Verifica se existe produto cadastrado
    for chave in estoque_produtos.keys():
        if chave == int_codigo_produto:
            return estoque_produtos[int_codigo_produto]
    return False


def buscar_pedido_por_codigo(int_codigo_pedido):
    # Verifica se existe produto cadastrado
    for chave in pedidos.keys():
        if chave == int_codigo_pedido:
            return pedidos[int_codigo_pedido]
    return False


def cadastrar_cliente():
    cliente_nome = str(input('insira o nome do cliente a cadastrar'))
    cliente_telefone = str(input('insira o telefone do cliente a cadastrar'))
    cliente_idade = str(input('insira a idade do cliente a cadastrar'))
    cliente_genero = str(input('insira o genero do cliente a cadastrar M ou F ou NB'))
    cliente_endereco = cadastrar_endereco()
    return Pessoa(cliente_nome, cliente_telefone, cliente_idade, cliente_genero, cliente_endereco)


def cadastrar_funcionario():
    funcionario_nome = str(input('insira o nome do funcionario'))
    funcionario_telefone = str(input('insira o telefone do funcionario'))
    funcionario_idade = str(input('insira a idade do funcionario'))
    funcionario_genero = str(input('insira o genero do funcionario M ou F ou NB'))
    funcionario_endereco = cadastrar_endereco()
    return Pessoa(funcionario_nome, funcionario_telefone, funcionario_idade, funcionario_genero, funcionario_endereco)


# Aplicação de exemplo disciplina POO - UFRB
# Sistema de controle de pedidos
# Professor Guilherme Braga Araújo
historico_notas =[]
estoque_produtos = {}
pedidos = {}

while True:
    # menu_principal
    opcao_escolhida = menu_principal()
    # verificando escolha
    # opc sair
    if (opcao_escolhida == "s"):
        break
    # opc 1
    elif (opcao_escolhida == "1"):
        while True:

            #implementar: visualizador de pedidos e nova opção de selecionar pedidos em aberto(?)

            opcao_escolhida = menu_pedido()
            # opc menu vendas - novo pedido
            if (opcao_escolhida == "1"):
                pedido = pedido_adicionar()
                if (pedido):
                    # adiciona pedido ao sistema
                    pedidos[pedido._codigo_pedido] = pedido
            # opc menu vendas - adicionar item    
            elif (opcao_escolhida == "2"):
                pedido_adicionar_item()
            elif (opcao_escolhida == "3"):
                pedido_remover_item()
            elif (opcao_escolhida == "4"):
                pedido_listar_items()
            elif (opcao_escolhida == "5"):
                finalizar_pedido()
            elif (opcao_escolhida == "6"):
                exibe_notas()
            else:
                # Volta para o menu principal
                break

    # opc 2
    elif (opcao_escolhida == "2"):
        produto = cadastrar_produto()
        if (produto):
            # adiciona produto ao nosso estoque
            estoque_produtos[produto._codigo_produto] = produto
    # opc 3
    elif (opcao_escolhida == "3"):
        remover_produto()
    # opc 4
    elif (opcao_escolhida == "4"):
        int_codigo_produto = int(input('Informe o código do produto para busca: '))
        produto_pesquisa = buscar_produto_por_codigo(int_codigo_produto)
        if (produto_pesquisa):
            print("Produto encontrado:")
            print(">Código=" + str(produto_pesquisa._codigo_produto))
            print(">Descricao=" + produto_pesquisa._descricao)
            print(">Valor=" + str(produto_pesquisa._preco))
            print(">Validade=" + str(produto_pesquisa._validade))
        else:
            print("Produto nâo cadastrado/encontrado.")
    else:
        print("A opção escolhida é inválida.")
