# main.py

import auth as user
import animal as fa
import produtos as pd
import relatorios as rl

fa.iniciarArquivo()
pd.iniciarArquivo()


def menuRelatorios():

    while True:

        print("\n===== RELATÓRIOS =====")
        print("1 - Relatório de vendas")
        print("2 - Total faturado")
        print("3 - Estoque baixo")
        print("4 - Quantidade de animais")
        print("5 - Exportar produtos CSV")
        print("6 - Exportar animais CSV")
        print("0 - Voltar")

        op = input("Digite a opção: ").strip()
        if op == "1":rl.relatorioVendas()
        elif op == "2":rl.totalFaturado()
        elif op == "3":rl.produtosEstoqueBaixo()
        elif op == "4":rl.quantidadeAnimais()
        elif op == "5":rl.exportarProdutosCSV()
        elif op == "6":rl.exportarAnimaisCSV()
        elif op == "0":
            break

def iniciarMenuCliente(nome_do_usuario):

    while True:

        print('\n==================== MENU CLIENTE ====================')
        print('1 - VER PRODUTOS DISPONÍVEIS')
        print('2 - COMPRAR PRODUTO')
        print('3 - VER ANIMAIS DISPONÍVEIS')
        print('4 - COMPRAR ANIMAIS')
        print('0 - RETORNAR MENU INICIAL')
        print('======================================================')

        op = input('Digite a opção: ').strip()

        if op == "1":pd.listarProdutos()
        elif op == "2":pd.venderProduto(nome_do_usuario)
        elif op == "3":fa.listarAnimais()
        elif op == "4":fa.comprarAnimal(nome_do_usuario)
        elif op == "0":
            print("Retornando ao menu inicial...")
            break

        else:
            print("Opção inválida!")


def iniciarMenuAdministrador():

    while True:

        print('\n==================== MENU ANIMAIS ====================')
        print('1 - CADASTRAR ANIMAL')
        print('2 - BUSCAR ANIMAL POR BRINCO')
        print('3 - LISTAR ANIMAIS')
        print('4 - ALTERAR ANIMAL')
        print('5 - REMOVER ANIMAL')

        print('\n==================== MENU PRODUTOS ====================')
        print('6 - CADASTRAR PRODUTO')
        print('7 - LISTAR PRODUTO')
        print('8 - ALTERAR PRODUTO')
        print('9 - REMOVER PRODUTO')
        print('10 - RELATÓRIOS')
        print('0 - RETORNAR MENU INICIAL')
        print('======================================================')

        op = input('Digite a opção: ').strip()

        if op == "1":fa.cadastrarAnimal()

        elif op == "2":
            brinco = input('Digite o brinco: ').strip()
            fa.buscarAnimalPorBrinco(brinco)

        elif op == "3":fa.listarAnimais()

        elif op == "4":
            brinco = input('Digite o brinco que deseja alterar: ').strip()
            fa.alterarAnimal(brinco)

        elif op == "5":
            brinco = input('Digite o brinco que deseja apagar: ').strip()
            fa.apagarAnimal(brinco)

        elif op == "6":pd.cadastrarProduto()

        elif op == "7":pd.listarProdutos()

        elif op == "8":
            codigo = input('Digite o código do produto: ').strip()
            pd.alterarProduto(codigo)

        elif op == "9":
            codigo = input('Digite o código do produto: ').strip()
            pd.apagarProduto(codigo)

        elif op == "10":menuRelatorios()

        elif op == "0":
            fa.salvarArquivo()
            pd.salvarArquivo()

            print("Retornando ao menu inicial...")

            break

        else:
            print("Opção inválida!")


def menuPrincipal():

    while True:

        print('\n======================')
        print('    FAZENDA SERTÃO')
        print('======================')
        print('1 - CADASTRAR USUÁRIO')
        print('2 - FAZER LOGIN')
        print('0 - SAIR')
        print('======================')

        opcao = input('Digite a opção: ').strip()
        if opcao == '1':

            user.menu_user_cadastrar()

        elif opcao == '2':

            dados_usuario = (user.menu_user_login())

            if dados_usuario:

                if (dados_usuario["tipo"] == "ADMINISTRADOR"):

                    iniciarMenuAdministrador()

                elif (dados_usuario["tipo"] == "CLIENTE"):

                    iniciarMenuCliente(dados_usuario["nome"])

            else:
                print("\nUsuário ou senha inválidos.")

        elif opcao == '0':

            fa.salvarArquivo()
            pd.salvarArquivo()

            print('\nSistema encerrado. Até logo!')

            break

        else:
            print('\nOpção inválida! ''Digite 1, 2 ou 0.')

# Inicialização do sistema
menuPrincipal()