usuarios = [
    ['admin', '123', 1],
    ['cliente', '123', 2]
]

animais = []

produtos = []

agendamentos = []

while True:

    # MENU PRINCIPAL

    print('\n======================')
    print('FAZENDA SERTÃO')
    print('======================')
    print('1 - Cadastrar usuário')
    print('2 - Login')
    print('3 - Sair')

    opcao = input('Digite a opção: ')

    if opcao == '1':

        nome = input('Digite o usuário: ')
        senha = input('Digite a senha: ')

        tipo = input('Tipo 1 - ADM 2 - CLIENTE: ')

        if tipo.isdigit():

            tipo = int(tipo)

            if tipo == 1 or tipo == 2:

                u = [nome, senha, tipo]

                usuarios.append(u)

                print('Usuário cadastrado')

            else:
                print('Tipo inválido')

        else:
            print('Tipo inválido')

    elif opcao == '2':

        nome = input('Usuário: ')
        senha = input('Senha: ')

        if nome == '' or senha == '':

            print('Login e senha não podem ser vazios')

        else:

            logado = False
            usuario = []

            for u in usuarios:

                if u[0] == nome and u[1] == senha:

                    logado = True
                    usuario = u
                    break

            if logado:

                # MENU ADMINISTRADOR

                if usuario[2] == 1:

                    while True:

                        print('\n===================')
                        print('MENU ADMINISTRADOR')
                        print('===================')
                        print('1 - Cadastrar animal')
                        print('2 - Listar animais')
                        print('3 - Atualizar animal')
                        print('4 - Remover animal')
                        print('5 - Cadastrar produto')
                        print('6 - Ver estoque')
                        print('7 - Ver agendamentos')
                        print('8 - Sair')

                        op = input('Digite a opção: ')

                        if op == '1':

                            tipo = input('Tipo do animal - Ex: bovino, caprino, suino: ')

                            brinco = input('Número/brinco - Ex: 1,2,3...: ')
                            
                            status = input('Status - Ex: em lactação, engorda, venda: ')

                            a = [tipo, brinco, status]

                            animais.append(a)

                            print('Animal cadastrado')

                        elif op == '2':

                            print('\nLISTA DE ANIMAIS')

                            for a in animais:

                                print('Tipo:', a[0])
                                print('Brinco:', a[1])
                                print('Status:', a[2])
                                print('----------------')

                        elif op == '3':

                            brinco = input('Digite o brinco: ')

                            for a in range(len(animais)):

                                if animais[a][1] == brinco:

                                    novo = input('Novo status: ')

                                    animais[a][2] = novo

                                    print('Animal atualizado')

                        elif op == '4':

                            brinco = input('Digite o brinco: ')

                            for a in animais:

                                if a[1] == brinco:

                                    animais.remove(a)

                                    print('Animal removido')

                                    break

                        elif op == '5':

                            nome = input('Nome do produto - Ex: queijo coalho, queijo manteiga: ')
                            qtd = float(input('Quantidade: '))
                            valor = float(input('Valor: '))

                            p = [nome, qtd, valor]

                            produtos.append(p)

                            print('Produto cadastrado')

                        elif op == '6':

                            print('\nESTOQUE')

                            for p in produtos:

                                print('Produto:', p[0])
                                print('Quantidade:', p[1])
                                print('Valor:', p[2])
                                print('----------------')

                        elif op == '7':

                            print('\nAGENDAMENTOS')

                            if len(agendamentos) == 0:

                                print('Nenhum agendamento encontrado')

                            else:

                                for a in agendamentos:

                                    print('Cliente:', a[0])
                                    print('Produto:', a[1])
                                    print('Data:', a[2])
                                    print('Hora:', a[3])
                                    print('----------------')

                        elif op == '8':

                            print('Saindo do sistema')

                            break

                        else:

                            print('Opção inválida')

                # MENU CLIENTE

                elif usuario[2] == 2:

                    while True:

                        print('\n===================')
                        print('MENU CLIENTE')
                        print('===================')
                        print('1 - Ver produtos')
                        print('2 - Ver animais')
                        print('3 - Comprar produto')
                        print('4 - Agendar retirada')
                        print('5 - Sair')

                        op = input('Digite a opção: ')

                        if op == '1':

                            print('\nPRODUTOS')

                            for p in produtos:

                                print('Produto:', p[0])
                                print('Quantidade:', p[1])
                                print('Valor:', p[2])
                                print('----------------')

                        elif op == '2':

                            print('\nLISTA DE ANIMAIS')

                            for a in animais:

                                print('Tipo:', a[0])
                                print('Brinco:', a[1])
                                print('Status:', a[2])
                                print('----------------')

                        elif op == '3':

                            nome_produto = input('Nome do produto: ')
                            qtd = float(input('Quantidade: '))

                            for p in range(len(produtos)):

                                if produtos[p][0] == nome_produto:

                                    if produtos[p][1] >= qtd:

                                        produtos[p][1] = produtos[p][1] - qtd

                                        print('Compra realizada')

                                    else:

                                        print('Estoque insuficiente')

                        elif op == '4':

                            produto = input('Produto: ')
                            data = input('Data: ')
                            hora = input('Hora: ')

                            a = [usuario[0], produto, data, hora]

                            agendamentos.append(a)

                            print('Retirada agendada')

                        elif op == '5':

                            print('Saindo do sistema')

                            break

                        else:

                            print('Opção inválida')

            else:

                print('Usuário inválido')

    elif opcao == '3':

        print('Sistema encerrado')

        break

    else:

        print('Opção inválida')