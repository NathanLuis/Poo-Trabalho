with open('produtos.txt', 'w') as arquivo:
    while True:
        codigo_produto = input('Informe o codigo do produto (Ou se já terminou digite "sair"): ')
        if codigo_produto != 'sair':
            arquivo.write(codigo_produto + ';')
            arquivo.write('\n')

            descricao = input('Informe o nome do produto: ')
            arquivo.write(descricao + ';')
            arquivo.write('\n')

            preco = input('Informe o preco do produto (ex: 1.10): ')
            arquivo.write(preco + ';')
            arquivo.write('\n')

            validade = input('Informe a validade do produto (ex: 10/12/2024): ')
            arquivo.write(validade + ';')
            arquivo.write('\n')

        else:
            break