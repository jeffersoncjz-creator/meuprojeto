
from auth import cadastrausuario, login
import animal as fa


def iniciarMenuAnimais():
    print('\n==================== MENU ANIMAIS ====================')
    print('1 - CADASTRAR ANIMAL')
    print('2 - BUSCAR ANIMAL POR BRINCO')
    print('3 - LISTAR ANIMAIS')
    print('4 - ALTERAR ANIMAL')
    print('5 - REMOVER ANIMAL')
    print('0 - Voltar ao Menu Inicial')
    print('======================================================')

fa.iniciarArquivo()

while True:
    # MENU INICIAL (LOGIN / CADASTRO)
    print('\n======================')
    print('    FAZENDA SERTÃO    ') 
    print('======================')
    print('1 - Cadastrar usuário')
    print('2 - Login')
    print('3 - Sair')
    print('======================')

    # 1. LOOP DO MENU INICIAL: Repete até digitar 1, 2 ou 3
    while True:
        opcao = input('Digite a opção: ')
        if opcao in ['1', '2', '3']:
            break
        else:
            print('Opção inválida! Digite 1, 2 ou 3.\n')

    # OPÇÃO 1: CADASTRAR USUÁRIO
    if opcao == '1':
        nome = input('Digite o usuário: ')
        senha = input('Digite a senha: ')
        
        # 2. LOOP DO TIPO DE USUÁRIO: Repete até digitar 1 ou 2
        while True:
            tipo = input('Tipo (1 - ADMINISTRADOR | 2 - CLIENTE): ')
            if tipo in ['1', '2']:
                break
            else:
                print('Tipo inválido! Por favor, digite apenas 1 ou 2.\n')

        sucesso = cadastrausuario(nome, senha, tipo)
        if sucesso:
            print('\nUsuário cadastrado com sucesso!')
        else:
            print('\nEste nome de usuário já está cadastrado. Tente outro.')

    # OPÇÃO 2: LOGIN (ENTRAR NO SISTEMA DE ANIMAIS)
    elif opcao == '2':
        nome = input('Usuário: ')
        senha = input('Senha: ')
        
        usuario = login(nome, senha)
        
        if usuario:
            funcao = "ADMINISTRADOR" if usuario == "1" else "CLIENTE"
            print(f'\nBem-vindo, {nome}! Você está logado com sucesso como {funcao}!')
            
            # --- SUBMENU DOS ANIMAIS (SÓ ENTRA SE LOGAR) ---
            while True:
                iniciarMenuAnimais()
                opcao_animal = input('Digite a opção: ')
                
                if opcao_animal == '0':
                    fa.salvarArquivo()
                    print("\nDados dos animais salvos com sucesso!")
                    break
                elif opcao_animal == '1':
                    fa.cadastrarAnimal()
                elif opcao_animal == '2':
                    brinco = input('Digite o brinco do animal: ')
                    fa.buscarAnimalPorBrinco(brinco)
                elif opcao_animal == '3':
                    fa.listarAnimais()
                elif opcao_animal == '4':
                    brinco = input('Digite o brinco do animal que deseja alterar: ')
                    fa.alterarAnimal(brinco)
                elif opcao_animal == '5':
                    print('Para apagar informe o dado abaixo')
                    brinco = input('Digite o brinco do animal que deseja apagar: ')
                    fa.apagarAnimal(brinco)
                else:
                    print('Opção inválida!')
        else:
            print('\nUsuário ou senha incorretos.')


    elif opcao == '3':
        print('\nSistema encerrado. Até logo!')
        break