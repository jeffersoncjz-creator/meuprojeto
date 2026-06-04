from auth import cadastrausuario, login

while True:
    # MENU PRINCIPAL
    print('\n======================')
    print('    FAZENDA SERTÃO    ') 
    print('======================')
    print('1 - Cadastrar usuário')
    print('2 - Login')
    print('3 - Sair')
    print('======================')

    # 1. LOOP DO MENU PRINCIPAL: Repete até digitar 1, 2 ou 3
    while True:
        opcao = input('Digite a opção: ')
        if opcao in ['1', '2', '3']:
            break
        else:
            print('Opção inválida! Digite 1, 2 ou 3.\n')

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

        # CHAMA A FUNÇÃO E VERIFICA SE DEU CERTO:
        sucesso = cadastrausuario(nome, senha, tipo)
        
        if sucesso:
            print('\nUsuário cadastrado com sucesso!')
        else:
            print('\nEste nome de usuário já está cadastrado. Tente outro.')

    elif opcao == '2':
        nome = input('Usuário: ')
        senha = input('Senha: ')
        
        usuario = login(nome, senha)
        
        if usuario:
            funcao = "ADMINISTRADOR" if usuario == "1" else "CLIENTE"
            print(f'\nBem-vindo, {nome}! Você está logado com sucesso como {funcao}!')
        else:
            print('\nUsuário ou senha incorretos.')

    elif opcao == '3':
        print('\nSistema encerrado. Até logo!')
        break