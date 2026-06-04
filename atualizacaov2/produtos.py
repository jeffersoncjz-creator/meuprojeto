produtos = []

def cadastrarProduto(nome, precoVenda):
    produto = {
        "codigo": len(produtos) + 1,
        "nome": nome,
        "quantidade": 0,
        "precoVenda": precoVenda
    }
    produtos.append(produto)

def listarProdutos():
    for p in produtos:
        print(p["codigo"],' - ',p['nome'], ' - ', p['quantidade'])

def adicionarAoEstoque():
    listarProdutos()
    codigo = int(input('Digite o código do produto: '))
    for p in produtos:
        if p["codigo"] == codigo:
            quantidade = float(input('Digite a quantidade: '))
            p["quantidade"] += quantidade
            produtos[codigo-1] = p
            break

def removerDoEstoque():
    listarProdutos()
    codigo = int(input('Digite o código do produto: '))
    for p in produtos:
        if p["codigo"] == codigo:
            quantidade = float(input('Digite a quantidade: '))
            p["quantidade"] -= quantidade
            produtos[codigo-1] = p
            break      

while True:
    print("""
        # 1 - cadastrar produto (nome, quantidade, preço de venda)
        # 2 - listar produtos
        # 3 - Adicionar ao estoque
        # 4 - Remove do estoque
        # 0 - Sair
    """)
    op = int(input('Digite a opção: '))
    if op == 0:
        break
    elif op == 1:
        nome = input('Digite o nome do produto: ')
        precoVenda = input('Digite o preço de venda do produto: ')
        cadastrarProduto(nome, precoVenda)
    elif op == 2:
        listarProdutos()
    elif op == 3:
        adicionarAoEstoque()
    elif op == 4:
        removerDoEstoque()
    else:
        print('Opção inválida')