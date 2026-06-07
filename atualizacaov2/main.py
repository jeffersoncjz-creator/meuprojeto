# main.py
import auth as user
import animal as fa
import produtos as pd

fa.iniciarArquivo()
pd.iniciarArquivo()

def iniciarMenuCliente(nome_do_usuario):
    while True:
        print('\n==================== MENU CLIENTE ====================')
        print('1 - VER PRODUTOS DISPONÍVEIS')
        print('2 - COMPRAR PRODUTO')
        print('3 - VER ANIMAIS DISPONÍVEIS')
        print('4 - COMPRAR ANIMAIS')
        print('0 - RETORNAR MENU INICIAL')
        print('======================================================')

        while True:
            op = input('Digite a opção: ').strip()
            if op in ['1', '2','3','4', '0']:
                break
            else:
                print('Opção inválida! Digite novamente.\n')
        
        if   op == "1": pd.listarProdutos()
        elif op == "2": pd.venderProduto(nome_do_usuario)
        elif op == "3": fa.listarAnimais()
        elif op == "4": fa.comprarAnimal(nome_do_usuario)
        elif op == "0":
            print("Retornando ao menu inicial...")
            break

def iniciarMenuAnimais():
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
        print('9 - REMOVER DO ESTOQUE (APAGAR)')
        print('0 - RETORNAR MENU INICIAL')
        print('======================================================')

        while True:
            op = input('Digite a opção: ').strip()
            if op in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                break
            else:
                print('Opção inválida! Digite novamente.\n')
        
        if   op == "1": fa.cadastrarAnimal()
        elif op == "2": fa.buscarAnimalPorBrinco(input('  Digite o brinco: ').strip())
        elif op == "3": fa.listarAnimais()
        elif op == "4": fa.alterarAnimal(input('  Digite o brinco que deseja alterar: ').strip())
        elif op == "5": fa.apagarAnimal(input('  Digite o brinco que deseja apagar: ').strip())
        elif op == "6": pd.cadastrarProduto()
        elif op == "7": pd.listarProdutos()
        elif op == "8": pd.alterarProduto(input('  Digite o código do produto que deseja alterar: ').strip())
        elif op == "9": pd.apagarProduto(input('  Digite o código do produto que deseja apagar: ').strip())
        elif op == "0":
            fa.salvarArquivo()
            pd.salvarArquivo()
            print("Retornando ao menu inicial...")
            break

while True:
    # MENU INICIAL (LOGIN / CADASTRO)
    print('\n======================')
    print('    FAZENDA SERTÃO    ') 
    print('======================')
    print('1 - CADASTRAR USUÁRIO')
    print('2 - FAZER LOGIN')
    print('0 - SAIR')
    print('======================')

    while True:
        opcao = input('Digite a opção: ').strip()
        if opcao in ['1', '2', '0']:
            break
        else:
            print('Opção inválida! Digite 1, 2 ou 0.\n')

    if opcao == '1':
        user.menu_user_cadastrar()
    elif opcao == '2':
        
        usuario = user.menu_user_login()
        
        if usuario == "ADMINISTRADOR":
            iniciarMenuAnimais()
        elif usuario == "CLIENTE":
            
            nome_cliente = input('Confirme seu nome para o extrato de compras: ').strip()
            iniciarMenuCliente(nome_cliente) 
        else:
            print("Usuário não encontrado ou credenciais incorretas.")
            
    elif opcao == '0':
        print('\nSistema encerrado. Até logo!')
        break