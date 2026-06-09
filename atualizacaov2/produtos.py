from tabulate import tabulate
import relatorios as rt
from datetime import datetime
import csv
import os

ARQUIVO_VENDAS = "atualizacaov2/arquivos/vendas.csv"

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

    rt.registrar_movimentacao("ADMIN", 'ENTRADA ESTOQUE', nome, quantidade)

    print('\nProduto cadastrado com sucesso!\n')

def buscarProdutoPorNome(nome):

    tabela = []

    for p in produtos:

        if p['nome'].lower() == nome.lower():

            tabela.append([
                p['codigo'],
                p['nome'],
                f"R$ {float(p['valor']):.2f}",
                p['quantidade']])

    if not tabela:

        print("\nProduto não encontrado.\n")
        return

    print(tabulate(
            tabela,
            headers=[
                "Código",
                "Produto",
                "Valor",
                "Quantidade"
            ],
            tablefmt="grid"))

def listarProdutos():

    if not produtos:
        print("\nNenhum produto cadastrado.\n")
        return

    tabela = []

    for p in produtos:

        tabela.append([
            p['codigo'],
            p['nome'],
            f"R$ {float(p['valor']):.2f}",
            p['quantidade'] ])

    print("\nESTOQUE DE PRODUTOS\n")

    print(
        tabulate(
            tabela,
            headers=[
                "Código",
                "Produto",
                "Valor",
                "Quantidade"
            ],
            tablefmt="grid"))

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
            
            p = {"nome": nome, 
                "codigo": codigo_novo, 
                "valor": valor, 
                "quantidade": quantidade}
    
            produtos[posicao] = p
            print('\n\nProduto alterado com sucesso!\n\n')

            rt.registrar_movimentacao('ENTRADA ESTOQUE', nome, quantidade)

            return
    print('Produto não encontrado!')

def apagarProduto(codigo):
    for posicao in range(len(produtos)):
        if produtos[posicao]['codigo'] == codigo:
            produtos.pop(posicao)
            print('Produto removido com sucesso!')
            break


def venderProduto(nome_cliente):
    print('\n--- VENDA DE PRODUTO ---')

    listarProdutos()

    codigo = input(
        '\nDigite o código do produto que deseja comprar: '
    ).strip()
    
    for posicao in range(len(produtos)):
        if produtos[posicao]['codigo'] == codigo:
            try:
                qtd_venda = float(input(f"Quantidade em estoque: {produtos[posicao]['quantidade']}. Quanto deseja comprar? ").strip())
            except ValueError:
                print('Quantidade inválida!')
                return
                
            qtd_atual = float(produtos[posicao]['quantidade'])
            
            if qtd_venda > qtd_atual:
                print(f"\nErro: Estoque insuficiente! Você tentou comprar {qtd_venda}, mas só temos {qtd_atual} em estoque.")
                print("Venda cancelada!\n")
                return
            
            nova_qtd = qtd_atual - qtd_venda
            produtos[posicao]['quantidade'] = str(nova_qtd)
            
            preco_unitario = float(produtos[posicao]['valor'])
            total_pago = preco_unitario * qtd_venda
            arquivo_existe = os.path.exists(ARQUIVO_VENDAS)

            with open(ARQUIVO_VENDAS, "a", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                if not arquivo_existe:
                    escritor.writerow([
                        "tipo",
                        "cliente",
                        "item",
                        "quantidade",
                        "valor"
                    ])

                escritor.writerow([
                    "PRODUTO",
                    nome_cliente,
                    produtos[posicao]["nome"],
                    qtd_venda,
                    total_pago
                ])
                
            print(f"\nVenda realizada com sucesso para o cliente: {nome_cliente}!")
            print(f"Total a pagar: R$ {total_pago:.2f}\n")
            
            agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            nome_extrato = f"atualizacaov2/arquivos/extrato_{nome_cliente}.txt"
            with open(nome_extrato, "a", encoding="utf-8") as extrato:
                extrato.write("="*18 + "\n")
                extrato.write("EXTRATO DE COMPRA\n")
                extrato.write("="*18 + "\n")
                extrato.write(f"Data/Hora: {agora}\n")
                extrato.write(f"Cliente: {nome_cliente}\n")
                extrato.write(f"Produto: {produtos[posicao]['nome']}\n")
                extrato.write(f"Código: {produtos[posicao]['codigo']}\n")
                extrato.write(f"Quantidade Comprada: {qtd_venda}\n")
                extrato.write(f"Preço Unitário: R$ {preco_unitario:.2f}\n")
                extrato.write(f"Valor Total: R$ {total_pago:.2f}\n")
                extrato.write("="*36 + "\n\n")
            
            print(f"Extrato impresso e salvo em: {nome_extrato}")
            
            nome_do_produto = produtos[posicao]['nome']
            
            imprimir_comprovante_termico(nome_cliente, nome_do_produto, total_pago)

            rt.registrar_movimentacao(nome_cliente, 'VENDA', nome_do_produto, qtd_venda)
            salvarArquivo()
            return
            
    print('Produto não encontrado!')

def imprimir_comprovante_termico(nome_cliente, produto, valor):
    caminho_arquivo = f"atualizacaov2/arquivos/extrato_{nome_cliente}.txt"
    caminho_absoluto = os.path.abspath(caminho_arquivo)
    try:
        os.startfile(caminho_absoluto, "print")
        print("Documento enviado para a fila do Windows com sucesso!")
    except Exception as e:
        print(f"Erro ao tentar imprimir: {e}")


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