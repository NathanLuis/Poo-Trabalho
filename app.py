# Aplicação de exemplo disciplina POO - UFRB
# Sistema de controle de pedidos
# Professor Guilherme Braga Araújo


import os

from pyarrow import null
#importando classes
from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_pessoa import Pessoa
from class_produto import Produto
from class_nota import Nota
#importando biblioteca datetime para trabalhar com strings que representam datas
from datetime import datetime

#PARTE 1: Criando Funções

#Função Menu Principal: Quando chamada, dá ao usuário o controle sobre o código faz através de um sistema de if e elses
def menu_principal():  # MENU PRINCIPAL
    #Escreve o menu principal na tela para que o ususário possa ver e interagir
    print('''
        MENU Principal:
        [1] - Controle de vendas
        [2] - Cadastrar novo produto
        [3] - Remover um produto
        [4] - Pesquisar um produto
        [s] - Salvar e Sair
    ''')
    #esse return faz com que a saída dessa função quando chamada seja a resposta dada pelo usuário
    return str(input('Escolha uma opção: '))

#Função Menu Pedidos: Apresenta menu que controla o que fazer com pedidos. Esse menu reutiliza o mecanismo do anterior, um print para mostrar o menu na tela e um return usando as funções str e input para receber uma informação do usuário e usar ela como saída da função
def menu_pedido(): # MENU PEDIDOS
    print('''
        MENU Vendas:
        [1] - Abrir novo pedido
        [2] - Adicionar item ao pedido
        [3] - Remover item do pedido
        [4] - Listar itens do pedido em detalhes
        [5] - Finalizar pedido e imprimir
        [6] - Exibir histórico de notas fiscais
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

#Função Exibir Notas: Vai mostrar na tela todas as notas fiscais geradas pelo programa até o momento
def exibe_notas():
    try:
        count = 1
        #usando um for para exibir todas as posições de um vetor onde as notas são armazeadas em ordem
        if historico_notas: 
            for iterado in historico_notas:
                print('\nNota Nº ' + str(count))
                print(iterado.toString())
                count += 1
        else:
            print("Registro vazio!")
    except Exception as e:
        print(e)

#Função Adicionar Pedidos: Essa função vai criar e cadastrar novos pedidos
def pedido_adicionar():
    try:
        # código pedido gerado automaticamente
        endereco_pedido = cadastrar_endereco()
        
        # usa as funções int() e len() para calcular o tamanho da lista de pedidos e depois soma 1 a ela,
        # esse valor se torna o código do pedido, quando ele for adicionado a lista, seu código será também seu index
        # a numeração do pedido começa de 1 até n
        codido_pedido = int(len(pedidos)) + 1
        
        # Atráves desse return o código cria um objeto do tipo pedido
        return Pedido(codido_pedido, endereco_pedido)
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

#Função Exibir Pedidos Em Aberto: Mostra todos os pedidos cujo status não foi alterado para encerrado ainda
def exibe_pedidos_em_aberto():
    count = 1
    #usa um for e um if para verificar quais pedidos da lista "pedidos" tem seu status aberto ou não e exibe na tela apenas ps pedidos cujo status não foi alterado
    for iterado in pedidos.values():
        if iterado._status == 0:
            print('Aberto Nº ' + str(count))
            print(iterado.toString())
            count += 1

#Função Finalizar Pedido: Resumidamente, altera o status de um pedido para fechado e gera sua nota fiscal
def finalizar_pedido():
    try:
        # chama a função exibir pedidos em aberto para que o usuário possa ver que pedidos ainda não foram finalizados
        exibe_pedidos_em_aberto()
        
        # armazena o código do pedido numa variável "selecao"
        selecao = int(input('O pedido que está prestes a finalizar não poderá ser modificado! Insira o CODIGO do Pedido a finalizar: '))
        
        # muda o statsus do pedido cujo código é "selecao" para fechado, alterando o atributo status de 0 para 1
        for pedido in pedidos.values():
            if pedido._codigo_pedido == selecao and pedido._status == 1:
                print('Erro: O pedido já foi finalizado!')
                return
            
            if pedido._codigo_pedido == selecao:
                try:
                    pedido_atual = buscar_pedido_por_codigo(selecao)
                    pedido_atual._status = 1
                    print('Pedido finalizado com sucesso! \nAgora insira os dados do cliente e funcionário. \n')
                    
                    cliente_atual = cadastrar_cliente()
                    funcionario_atual = cadastrar_funcionario()
                    
                    # cria um objeto do tipo nota e armazena ele numa varíavel "nota_atual"
                    nota_atual = Nota(pedido_atual, cliente_atual, funcionario_atual)
                    print('Nota gerada com sucesso! \n' + nota_atual.toString())
                    
                    # adciona a nota armazenada na variável "nota_atual" a lista "historico_notas"
                    historico_notas.append(nota_atual)
                    pedido = None
                except Exception as e:
                    print(f"Erro ao processar o pedido: {e}")
                break
        else:
            print('Pedido não encontrado!')
    except ValueError:
        print("Erro: Código do pedido inválido.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        
#função Adicionar Item Ao Pedido: Vai criar um objeto do tipo item do pedido (classe complexa) e adicionar ele a um vetor contendo todos os itens do pedido
def pedido_adicionar_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para adicionar um novo item: '))
    #verifica se pedido existe usando ifs para validar o pedido baseado no seu código
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_produto = int(input('Informe o código do produto para adicionar ao pedido: '))
        #Usa o método buscar produdo por código para procurar se existe um objeto do tipo produto com o código pedido, o retorno dessa função é do tipo boleano
        produto = buscar_produto_por_codigo(int_codigo_produto)
        #esse if só roda se o produto existir, finalmente criando um item do pedido
        if produto:
            int_quantidade_item = int(input('Informe a quantidade do item: '))
            novo_item_pedido = ItemPedido(produto, int_quantidade_item)
            pedido.adicionar_item_ao_pedido(novo_item_pedido)
        else:
            print("Não foi possível adicionar este produto, pois o código do produto não existe!")
        # return Pedido(codido_pedido, endereco_pedido)
    else:
        print("Pedido inexistente")
        return False

#Função Remover Item do Pedido: Essa função apaga um objeto do tipo item do pedido da lista que armazena os itens de um determinado pedido
def pedido_remover_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para remover um item selecionado: '))
    # verifica se pedido existe
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_item = int(input('Informe o código do item para remover deste pedido ' + str(pedido._codigo_pedido) + ': '))
        # verifica se número item informado existe
        item_pedido = None
        for item in pedido._itens_pedidos:
            if item._produto._codigo_produto == int_codigo_item:
                item_pedido = pedido._itens_pedidos.index(item)
                break  # Exit the loop once the item is found
        if item_pedido is not None:
            pedido.remover_item_pedido(item_pedido)
            print("Item removido com sucesso!")
            return True
        else:
            print("Item não encontrado no pedido.")
    else:
        print("Pedido inexistente")
        return False
#função Listar Itens do Pedido: Exibe na tela todos os elementos da lista de itens de um determinado pedido
def pedido_listar_items():
    int_pedido_selecionado = int(input('Informe o código do pedido para mais detalhes: '))
    # verificar se pedido existe
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        #busca o pedido específico na lista de pedidos
        pedido = pedidos[int_pedido_selecionado]
        #a função tostring vai transformar numa string todos os itens do pedido selecionado pelo código e escrever na tela
        pedido.toString()
    else:
        print("Pedido inexistente")
        return False

#Função Cadastrar Endereço: pede ao usuário os dados que comporão os atributos de um objeto do tipo endereço e finaliza criando o tal objeto
def cadastrar_endereco():
    try:
        str_cep = str(input('Informe o cep do endereço: '))
        str_rua = str(input('Informe a rua: '))
        int_num = int(input('Informe o número: '))
        str_complemento = str(input('Informe o complemento do endereço: '))
        str_bairro = str(input('Informe o bairro: '))
        str_cidade = str(input('Informe a cidade: '))
        
        endereco = Endereco(str_cep, str_rua, int_num,
                            str_complemento, str_bairro, str_cidade)
        return endereco
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

#Função Cadastrar Produto: pede ao usuário os dados que comporão os atributos de um objeto do tipo produto e finaliza criando o tal obejto
def cadastrar_produto():
    try:
        int_codigo = int(input('Informe o código identificador do produto: '))
        for produto in estoque_produtos:
            if produto._codigo_produto == int_codigo:
                print("Produto já cadastrado!")
                return False
        str_nome = str(input('Qual o nome/descrição do produto? '))
        flt_preco = float(input('Informe o valor (ex. 0.00): '))
        date_validade = input('Informe a validade do produto (formato dd/mm/aaaa): ')
        date_validade = datetime.strptime(date_validade, '%d/%m/%Y')

        return Produto(int_codigo, str_nome, flt_preco, date_validade)
    except ValueError as e:
        print(f"Por favor, insira dados válidos.")
        return False
    except Exception as e:
        print(f" Tente novamente.")
        return False
#Função Remover Produdo: Busca um objeto do tipo produto pelo seu código e o apaga do dicionário estoque de produtos
def remover_produto():
    try:
        codigo_remocao = int(input('Informe o código do produto para remoção: '))
        produto_remover = None
        for produto in estoque_produtos:
            if produto._codigo_produto == codigo_remocao:
                produto_remover = produto
                break  # Interrompe o loop se o produto for encontrado

        if produto_remover:
            print("Produto (" + produto_remover._descricao + ") removido!")
            estoque_produtos.remove(produto_remover)
        else:
            print("Produto não encontrado!")

    except ValueError as e:
        print(f"Por favor, insira um código numérico válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}. Tente novamente.")
    
    

#Função Buscar Produto por Código: Informado o código de um produto, pesquisa o produto no dicionário estoque de produtos, isso se aproveita do fato de o código de um produto ser o seu index
def buscar_produto_por_codigo(int_codigo_produto):
    # Verifica se existe produto cadastrado
    for obj in estoque_produtos:
        if obj._codigo_produto == int_codigo_produto:
            return obj
    return False

#Função Buscar Pedido por Código: Informado o código de um pedido, pesquisa o pedido no dicionário pedidos, isso se aproveita do fato de o código de um pedido ser o seu index
def buscar_pedido_por_codigo(int_codigo_pedido):
    # Verifica se existe pedido cadastrado
    for chave in pedidos.keys():
        if chave == int_codigo_pedido:
            return pedidos[int_codigo_pedido]
    return False

#Função Cadastrar Cliente: pede ao usuário os dados que comporão os atributos de um objeto do tipo Cliente (que erda do tipo Pessoa) e finaliza criando o tal objeto

def cadastrar_cliente():
    cliente_nome = str(input('\ninsira o nome do cliente a cadastrar: '))
    cliente_telefone = str(input('insira o telefone do cliente a cadastrar: '))
    cliente_idade = str(input('insira a idade do cliente a cadastrar: '))
    cliente_genero = str(input('insira o genero do cliente a cadastrar (M ou F ou NB): '))
   #cliente_endereco = cadastrar_endereco()
    return Pessoa(cliente_nome, cliente_telefone, cliente_idade, cliente_genero, null)

#Função Cadastrar Funcionário: pede ao usuário os dados que comporão os atributos de um objeto do tipo Funcionário (que erda do tipo Pessoa) e finaliza criando o tal objeto
def cadastrar_funcionario():
    funcionario_nome = str(input('\ninsira o nome do funcionario: '))
    funcionario_telefone = str(input('insira o telefone do funcionario: '))
    funcionario_idade = str(input('insira a idade do funcionario: '))
    funcionario_genero = str(input('insira o genero do funcionario (M ou F ou NB): '))
    #funcionario_endereco = cadastrar_endereco()
    return Pessoa(funcionario_nome, funcionario_telefone, funcionario_idade, funcionario_genero, null)



def writeAndCleanSave_method(arquivo, registro):
    caminho_arquivo = os.path.join(os.getcwd(), f'{arquivo}_registro.txt')
    try:
        with open(caminho_arquivo, 'w') as file:
            if registro:
                for obj in registro:
                        if obj:
                            line = obj.toStringForSaveLoadMethod()
                            file.write(line + '\n')
            else:
                print((f'{registro} vazio, não há nada para salvar'))
    except IOError:
        print(f"Erro: Não foi possível escrever no arquivo {arquivo}.")


def readAndLoad_method(arquivo, registro, cls):
    caminho_arquivo = os.path.join(os.getcwd(), f'{arquivo}_registro.txt')
    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, 'r') as file:
                for line in file:
                    obj = cls.fromStringToSaveLoadMethod(line.strip())
                    if obj:
                        registro.append(obj)
        except FileNotFoundError:
            print("Não foram detectados registros anteriores. Iniciando novo registro.")
        except IOError:
            print("Erro: Não foi possível ler o arquivo.")
    else:
        print(f'O arquivo {caminho_arquivo} não existe. Iniciando novo registro.')






#Cria uma lista histórico_notas para armazernar as notas e dois dicionários, estoque_produtos e pedidos para adicionar os pedidos
historico_notas = []
estoque_produtos = []
pedidos = {}
readAndLoad_method('notas', historico_notas, Nota)
readAndLoad_method('produtos', estoque_produtos, Produto)

while True:
    # menu_principal
    opcao_escolhida = menu_principal()
    # verificando escolha
    # opc sair
    if (opcao_escolhida == "s"):
        for obj in historico_notas:
            print(obj.toString())
        for obj in estoque_produtos:
            print(obj.toStringForSaveLoadMethod())
        writeAndCleanSave_method('notas', historico_notas)
        writeAndCleanSave_method('produtos', estoque_produtos)
        #função de saving do sistema a implementar

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
                    pedidos[pedido._codigo_pedido]=pedido
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
            for obj in estoque_produtos:
                if obj._codigo_produto == produto._codigo_produto:
                    print("Produto já cadastrado!")
                    break
            estoque_produtos.append(produto)
            print("Produto cadastrado com sucesso!")
        else:
            print("Falha no cadastro do produto!")
            # adiciona produto ao nosso estoque
            
    # opc 3
    elif (opcao_escolhida == "3"):
        remover_produto()
    # opc 4
    elif (opcao_escolhida == "4"):
        try:
            int_codigo_produto = int(input('Informe o código do produto para busca: '))
            
            # Assume-se que a função buscar_produto_por_codigo pode gerar exceções
            produto_pesquisa = buscar_produto_por_codigo(int_codigo_produto)
            
            if produto_pesquisa:
                print("Produto encontrado:")
                print(">Código=" + str(produto_pesquisa._codigo_produto))
                print(">Descrição=" + produto_pesquisa._descricao)
                print(">Valor=" + str(produto_pesquisa._preco))
                print(">Validade=" + str(produto_pesquisa._validade))
            else:
                print("Produto não cadastrado/encontrado.")
        
        except ValueError:
            print("Erro: Código do produto deve ser um número inteiro.")
        
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o produto: {str(e)}")
    
    else:
        print("A opção escolhida é inválida.")
