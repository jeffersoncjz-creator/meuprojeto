usuarios = []

animais = []

produtos = []

agendamentos = []

while True:

    # MENU PRINCIPAL

    print('======================')
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
                usuario_existe = False

                for u in usuarios:

                    if u[0] == nome:

                        usuario_existe = True
                        break

                if usuario_existe:

                    print('Usuário já cadastrado')

                else:

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

                        print('===================')
                        print('MENU ADMINISTRADOR')
                        print('===================')
                        print('1 - Cadastrar animal')
                        print('2 - Listar animais')
                        print('3 - Atualizar animal')
                        print('4 - Remover animal')
                        print('5 - Cadastrar produto')
                        print('6 - Atualizar produto')
                        print('7 - Remover produto')
                        print('8 - Estoque de produtos')
                        print('9 - Ver agendamentos')
                        print('0 - Retornar ao menu inicial')

                        op = input('Digite a opção: ')

                        if op == '1':

                            brincos = []

                            for anm in animais:

                                brincos.append(anm[2])

                            tipo = input('Tipo do animal - Ex: bovino, caprino, suino: ')

                            brinco = input('Número/brinco - Ex: 1,2,3...: ')

                            while brinco in brincos:

                                print("ID brinco já cadastrado")

                                brinco = input('Número/brinco - Ex: 1,2,3...: ')
                            
                            status = input('Status - Ex: lactação, engorda, venda: ')

                            valor = float(input('Digite o valor do animal: '))

                            a = [tipo, 1, brinco, status, valor]

                            animais.append(a)

                            print('Animal cadastrado')

                        elif op == '2':

                            print('LISTA DE ANIMAIS')

                            for a in animais:

                                print('Tipo:', a[0])
                                print('Brinco:', a[2])
                                print('Status:', a[3])
                                print('Valor:', a[4])
                                print('----------------')

                        elif op == '3':

                            brinco = input('Digite o brinco: ')

                            for a in range(len(animais)):

                                if animais[a][2] == brinco:

                                    novo = input('Novo status: ')

                                    animais[a][3] = novo

                                    print('Animal atualizado')

                        elif op == '4':

                            brinco = input('Digite o brinco: ')

                            for a in animais:

                                if a[2] == brinco:

                                    animais.remove(a)

                                    print('Animal removido')

                                    break

                        elif op == '5':

                            nome = input('Nome do produto - Ex: leite, queijo coalho, queijo manteiga: ')
                            qtd = float(input('Quantidade: '))
                            valor = float(input('Valor: '))

                            p = [nome, qtd, valor]

                            produtos.append(p)

                            print('Produto cadastrado')

                        elif op == '6':

                            nome_produto = input('Digite o Produto: ')

                            encontrado = False

                            for a in range(len(produtos)):

                                if produtos[a][0] == nome_produto:

                                    novo = input('Novo nome do produto: ')

                                    produtos[a][0] = novo

                                    encontrado = True

                                    print('Produto atualizado')

                                    break
                            
                            if encontrado == False:

                                print('Produto não encontrado')

                        elif op == '7':

                            nome_produto = input('Digite o produto: ')

                            encontrado = False

                            for p in produtos:

                                if p[0] == nome_produto:

                                    produtos.remove(p)

                                    encontrado = True

                                    print('Produto removido')

                                    break

                            if encontrado == False:

                                print('Produto não encontrado')

                        elif op == '8':

                            print('ESTOQUE DE PRODUTOS')

                            for p in produtos:

                                print('Produto:', p[0])
                                print('Quantidade:', p[1])
                                print('Valor:', p[2])
                                print('----------------')

                        elif op == '9':

                            print('AGENDAMENTOS')

                            if len(agendamentos) == 0:

                                print('Nenhum agendamento encontrado')

                            else:

                                for a in agendamentos:

                                    print('Cliente:', a[0])
                                    print('Produto:', a[1])
                                    print('Data:', a[2])
                                    print('Hora:', a[3])
                                    print('----------------')

                        elif op == '0':

                            print('Saindo do sistema')

                            break

                        else:

                            print('Opção inválida')

                # MENU CLIENTE

                elif usuario[2] == 2:

                    while True:

                        print('===================')
                        print('MENU CLIENTE')
                        print('===================')
                        print('1 - Ver produtos')
                        print('2 - Ver animais')
                        print('3 - Comprar produto')
                        print('4 - Comprar animal')
                        print('5 - Agendar retirada')
                        print('6 - Retornar ao menu inicial')

                        op = input('Digite a opção: ')

                        if op == '1':

                            print('PRODUTOS')

                            if len(produtos) == 0:

                                print('----------------')
                                print("Nenhum Produto Disponível")
                                print('----------------')

                            for p in produtos:

                                print('----------------')
                                print('Produto:', p[0])
                                print('Quantidade:', p[1])
                                print('Valor:', p[2])
                                print('----------------')

                        elif op == '2':

                            print('LISTA DE ANIMAIS')


                            if len(animais) == 0:
                                print('----------------')
                                print("Nenhum Animal Disponível")
                                print('----------------')

                            for a in animais:

                                print('Tipo:', a[0])
                                print('Brinco:', a[2])
                                print('Status:', a[3])
                                print('Valor:', a[4])
                                print('----------------')

                        elif op == '3':
                            if len(produtos) > 0:
                                print("Produtos Disponíveis")
                                for p in produtos:
                                    print('----------------')
                                    print('Produto:', p[0])
                                    print('Quantidade:', p[1])
                                    print('Valor:', p[2])
                                    print('----------------')


                                nome_produto = input('Nome do produto: ')
                                qtd = float(input('Quantidade: '))

                                for p in range(len(produtos)):

                                    if produtos[p][0] == nome_produto:

                                        if produtos[p][1] >= qtd:

                                            produtos[p][1] = produtos[p][1] - qtd

                                            print('Compra realizada')

                                        else:

                                            print('Estoque insuficiente')
                            else:
                                print('----------------')
                                print("Nenhum Produto Disponível")
                                print('----------------')

                        elif op == '4':
                            if len(animais) > 0:
                                print("Animais Disponíveis")
                                for a in animais:
                                    print('----------------')
                                    print('Tipo:', a[0])
                                    print('Brinco:', a[2])
                                    print('Status:', a[3])
                                    print('Valor:', a[4])
                                    print('----------------')


                                nome_animais = input('Nome do animal: ')
                                #qtd = float(input('Quantidade: '))

                                for a in range(len(animais)):

                                    if animais[a][0] == nome_animais:

                                        if animais[a][1] >= qtd:

                                            animais[a][1] = animais[a][1] - 1
                                            print('Compra realizada') 

                                        else:

                                            print('Estoque insuficiente')
                            else:
                                print('----------------')
                                print("Nenhum Animal Disponível")
                                print('----------------')

                        elif op == '5':

                            produto = input('Produto: ')
                            data = input('Data: ')
                            hora = input('Hora: ')

                            a = [usuario[0], produto, data, hora]

                            agendamentos.append(a)

                            print('Retirada agendada')

                        elif op == '6':

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