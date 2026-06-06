produtos = []

def cadastrarProduto():
    print('\n--- CADASTRO DE PRODUTO ---')
    codigo = input('Digite o código do produto: ').strip()
    
    for p in produtos:
        if p['codigo'] == codigo:
            print(f'\nO código "{codigo}" já está cadastrado para o produto "{p["nome"]}".')
            print('Cadastro cancelado!\n')
            return
            
    nome = input('Digite o nome do produto: ').strip()
    valor = input('Digite o valor do produto: ').strip()
    quantidade = input('Digite a quantidade inicial em estoque: ').strip()
    
    novo_produto = {
        "nome": nome, 
        "codigo": codigo, 
        "valor": valor, 
        "quantidade": quantidade
    }
    produtos.append(novo_produto)
    print('\nProduto cadastrado com sucesso!\n')

def buscarProdutoPorNome(nome):
    print('-' * 50)
    for p in produtos:
        if p['nome'] == nome:
            print(p['nome'], ' | ', p['codigo'], ' | ', p['valor'], ' | Qtd: ', p['quantidade']) 
    print('-' * 50)

def listarProdutos():
    print('-' * 50)
    for p in produtos:
        print(p['nome'], ' | ', p['codigo'], ' | ', p['valor'], ' | Qtd: ', p['quantidade']) 
    print('-' * 50)

def alterarProduto(codigo):
    print('Para alterar informe o dado abaixo')
    for posicao in range(len(produtos)):
        if produtos[posicao]['codigo'] == codigo:
            nome = input('Digite o novo nome: ').strip()
            codigo_novo = input('Digite o novo código: ').strip()
            
            if codigo_novo != codigo:
                for p in produtos:
                    if p['codigo'] == codigo_novo:
                        print(f'\nO código "{codigo_novo}" já pertence a outro produto. Alteração cancelada!\n')
                        return

            valor = input('Digite o novo valor: ').strip()
            quantidade = input('Digite a nova quantidade: ').strip()
            
            p = {
                "nome": nome, 
                "codigo": codigo_novo, 
                "valor": valor, 
                "quantidade": quantidade
            }
    
            produtos[posicao] = p
            print('\n\nProduto alterado com sucesso!\n\n')
            return
    print('Produto não encontrado!')

def apagarProduto(codigo):
    for posicao in range(len(produtos)):
        if produtos[posicao]['codigo'] == codigo:
            produtos.pop(posicao)
            print('Produto removido com sucesso!')
            break

def salvarArquivo():
    with open("atualizacaov2/arquivos/produtos.txt", "w", encoding="utf-8") as arq:
        for p in produtos:
            arq.write(f'{p["nome"]},{p["codigo"]},{p["valor"]},{p["quantidade"]}\n')

def iniciarArquivo():
    try:
        with open("atualizacaov2/arquivos/produtos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
            for c in conteudo:
                c = c.replace('\n', '')
                dados = c.split(',')
                if len(dados) >= 4:
                    nome = dados[0]
                    codigo = dados[1]
                    valor = dados[2]
                    quantidade = dados[3]
                    produtos.append({
                        "nome": nome,
                        "codigo": codigo,
                        "valor": valor,
                        "quantidade": quantidade
                    })
    except FileNotFoundError:
        with open("atualizacaov2/arquivos/produtos.txt", "w", encoding="utf-8") as arquivo:
            pass