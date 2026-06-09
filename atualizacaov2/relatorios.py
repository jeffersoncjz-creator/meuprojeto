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
            escritor.writerow(["Data", "Usuario", "Acao", "Item", "Qtd"]) # Adicionada coluna Usuario
        return

    with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            historico.append({
                "data": linha["Data"],
                "usuario": linha["Usuario"], # Adicionado
                "acao": linha["Acao"],
                "item": linha["Item"],
                "qtd": linha["Qtd"]
            })

def salvarArquivoHistorico():
    """Salva a lista de histórico no arquivo CSV."""
    with open(ARQUIVO_HISTORICO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Data", "Usuario", "Acao", "Item", "Qtd"])
        for h in historico:
            escritor.writerow([h["data"], h["usuario"], h["acao"], h["item"], h["qtd"]])

def registrar_movimentacao(usuario, acao, item, qtd):
    data_atual = datetime.now().strftime('%d/%m %H:%M')
    
    novo_registro = {
        'data': data_atual,
        'usuario': usuario, 
        'acao': acao.upper(),
        'item': item,
        'qtd': str(qtd)
    }
    
    historico.append(novo_registro)
    salvarArquivoHistorico()
    
    historico.append(novo_registro)
    salvarArquivoHistorico()

def listar_historico():
    """Exibe o relatório de movimentação."""
    if not historico:
        print("\nNenhuma movimentação registrada no histórico.\n")
        return

    tabela = []
    for h in historico:
        tabela.append([h['data'], h['usuario'], h['acao'], h['item'], h['qtd']])

    print("\n================ HISTÓRICO DE MOVIMENTAÇÃO ================")
    print(
        tabulate(
            tabela,
            headers=["Data/Hora", "Usuário", "Ação", "Item", "Quantidade"],
            tablefmt="grid"
        )
    )
    confirmacao = input("Deseja imprimir este relatório na impressora térmica? (s/n): ").strip().lower()
    
    if confirmacao == 's':
        imprimir_historico_termico()

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

    confirmacao = input("Deseja imprimir este relatório na impressora térmica? (s/n): ").strip().lower()
    
    if confirmacao == 's':
        imprimir_relatorio_vendas_termico()

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

def imprimir_historico_termico():
    caminho_arquivo = "atualizacaov2/arquivos/historico_imprimir.txt"
    
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write("=== HISTORICO DE MOVIMENTACAO ===\n\n")
        for h in historico:
            f.write(f"Data: {h['data']} | Usuário: {h['usuario']}\n")
            f.write(f"Ação: {h['acao']} | Item: {h['item']} (Qtd: {h['qtd']})\n")
            f.write("-" * 32 + "\n")
    
    try:
        os.startfile(os.path.abspath(caminho_arquivo), "print")
        print("\nRelatório enviado para a impressora!")
    except Exception as e:
        print(f"\nErro ao imprimir: {e}")

def imprimir_relatorio_vendas_termico():
    if not os.path.exists(ARQUIVO_VENDAS):
        print("\nNenhuma venda para imprimir.\n")
        return

    caminho_arquivo = "atualizacaov2/arquivos/vendas_imprimir.txt"
    total_faturado = 0
    
    with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as f_leitura:
        leitor = csv.reader(f_leitura)
        cabecalho = next(leitor, None)
        
        with open(caminho_arquivo, "w", encoding="utf-8") as f_escrita:
            f_escrita.write("=== RELATORIO DE VENDAS ===\n\n")
            
            for linha in leitor:
                
                tipo, cliente, item, qtd, valor = linha
                f_escrita.write(f"Cliente: {cliente}\n")
                f_escrita.write(f"Item: {item} | Qtd: {qtd}\n")
                f_escrita.write(f"Valor: R$ {valor.replace('.', ',')}\n")
                f_escrita.write("-" * 32 + "\n")
                total_faturado += float(valor)
            
            f_escrita.write(f"\nTOTAL FATURADO: R$ {total_faturado:.2f}".replace('.', ','))
            f_escrita.write("\n\n")

    try:
        os.startfile(os.path.abspath(caminho_arquivo), "print")
        print("\nRelatório de vendas enviado para a impressora!")
    except Exception as e:
        print(f"\nErro ao imprimir: {e}")