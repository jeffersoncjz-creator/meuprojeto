from datetime import datetime
from tabulate import tabulate
import produtos
import animal
import csv
import os

ARQUIVO_VENDAS = "atualizacaov2/arquivos/vendas.csv"
ARQUIVO_HISTORICO = "atualizacaov2/arquivos/historico.csv"

historico = []


def iniciarArquivoHistorico():
    """Lê o histórico salvo no arquivo CSV ao iniciar o programa."""
    if not os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow(["Data", "Acao", "Item", "Qtd"])
        return

    with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            historico.append({
                "data": linha["Data"],
                "acao": linha["Acao"],
                "item": linha["Item"],
                "qtd": linha["Qtd"]
            })

def salvarArquivoHistorico():
    """Salva a lista de histórico no arquivo CSV."""
    with open(ARQUIVO_HISTORICO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Data", "Acao", "Item", "Qtd"])
        for h in historico:
            escritor.writerow([h["data"], h["acao"], h["item"], h["qtd"]])

def registrar_movimentacao(acao, item, qtd):
    """Função chamada pelos outros arquivos para registrar a alteração."""
    data_atual = datetime.now().strftime('%d/%m %H:%M')
    
    novo_registro = {
        'data': data_atual,
        'acao': acao.upper(),
        'item': item,
        'qtd': str(qtd)
    }
    
    historico.append(novo_registro)
    salvarArquivoHistorico()

def listar_historico():
    """Exibe o relatório de movimentação formatado com tabulate."""
    if not historico:
        print("\nNenhuma movimentação registrada no histórico.\n")
        return

    tabela = []
    for h in historico:
        tabela.append([h['data'], h['acao'], h['item'], h['qtd']])

    print("\n================ HISTÓRICO DE MOVIMENTAÇÃO ================")
    print(
        tabulate(
            tabela,
            headers=["Data/Hora", "Ação", "Item", "Quantidade"],
            tablefmt="grid"
        )
    )
    print("===========================================================\n")


def relatorioVendas():
    if not os.path.exists(ARQUIVO_VENDAS):
        print("\nNenhuma venda registrada.\n")
        return

    tabela = []
    with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor, None)
        for linha in leitor:
            tabela.append(linha)

    print(
        tabulate(
            tabela,
            headers=["Tipo", "Cliente", "Item", "Qtd", "Valor"],
            tablefmt="grid"
        )
    )

def totalFaturado():
    total = 0
    if not os.path.exists(ARQUIVO_VENDAS):
        print("\nNenhuma venda registrada.\n")
        return

    with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor, None)
        for linha in leitor:
            total += float(linha[4])

    print(f"\nTOTAL FATURADO: R$ {total:.2f}\n")

def produtosEstoqueBaixo(limite=5):
    tabela = []
    for p in produtos.produtos:
        try:
            qtd = float(p["quantidade"])
            if qtd <= limite:
                tabela.append([p["codigo"], p["nome"], qtd])
        except:
            pass

    if not tabela:
        print("\nNenhum produto com estoque baixo.\n")
        return

    print(
        tabulate(
            tabela,
            headers=["Código", "Produto", "Quantidade"],
            tablefmt="grid"
        )
    )

def quantidadeAnimais():
    print(f"\nQuantidade de animais cadastrados: {len(animal.animais)}\n")

def exportarProdutosCSV():
    with open("atualizacaov2/arquivos/produtos_export.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["codigo", "nome", "valor", "quantidade"])
        for p in produtos.produtos:
            escritor.writerow([p["codigo"], p["nome"], p["valor"], p["quantidade"]])
    print("\nProdutos exportados com sucesso!\n")

def exportarAnimaisCSV():
    with open("atualizacaov2/arquivos/animais_export.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["brinco", "nome", "valor"])
        for a in animal.animais:
            escritor.writerow([a["brinco"], a["nome"], a["valor"]])
    print("\nAnimais exportados com sucesso!\n")