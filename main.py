usuarios = []
rebanho = []  
producao = []
agendamentos = []

while True:
    print("\n" + "="*40)
    print("      APP FAZENDA SERTÃO")
    print("="*40)
    print("1 - Efetuar login no App")
    print("2 - Cadastrar novo Usuario")
    print("0 - Sair\n")

    menu = input("Digite a opção desejada! ")

    if menu == "0":
        print("Encerrando...")
        break
    
    elif menu == "1":
        login = input("Login: ")
        senha = input("Senha: ")
        encontrado = False
        usuario_atual = None

        for i in usuarios:
            if i[0] == login and i[1] == senha:
                encontrado = True
                usuario_atual = i
                print(f"\nBem-vindo, {login}!")
                break

        if encontrado:
            while True:
                print("\n" + "="*40)
                print(f"   MENU PRINCIPAL - {login}")
                print("="*40)
                
                if usuario_atual[2] == "1":
                    print("1 - Gerenciar Rebanho (ADM)")
                    print("2 - Gerenciar Produção (ADM)")
                else:
                    print("3 - Efetuar Compra (Cliente)")
                    print("4 - Agendar Retirada (Cliente)")
                
                print("0 - Logout (Sair)")

                opcao_logado = input("Escolha uma opção: ")

                if opcao_logado == "0":
                    break

                elif opcao_logado == "1" and usuario_atual[2] == "1":
                    print("\n--- CADASTRAR NO REBANHO ---")
                    tipo_a = input("Tipo do animal: ")
                    id_a = input("ID (Brinco): ")
                    status_a = input("Status: ")
                    rebanho.append([tipo_a, id_a, status_a])
                    print("Animal cadastrado com sucesso!")

                elif opcao_logado == "2" and usuario_atual[2] == "1":
                    print("\n--- CADASTRAR PRODUÇÃO ---")
                    item = input("Produto: ")
                    qtd = int(input("Quantidade em estoque (número): "))
                    valor = input("Valor de venda: R$ ")
                    producao.append([item, qtd, valor])
                    print("Estoque atualizado!")

                elif opcao_logado == "3" and usuario_atual[2] == "2":
                    print("\n--- PRODUTOS DISPONÍVEIS ---")
                    posicao = 0
                    for p in producao:
                        print(f"{posicao} - {p[0]} | Disponível: {p[1]} | Preço: {p[2]}")
                        posicao = posicao + 1
                    
                    if len(producao) == 0:
                        print("Não há produtos no estoque.")
                    else:
                        escolha = int(input("\nDigite o número do produto: "))
                        qtd_compra = int(input("Quanto deseja comprar? "))
                        
                        if escolha < len(producao):
                            if producao[escolha][1] >= qtd_compra:
                                producao[escolha][1] = producao[escolha][1] - qtd_compra
                                print(f"\nCompra de {qtd_compra} unidade(s) realizada!")
                            else:
                                print("\nQuantidade insuficiente no estoque!")
                        else:
                            print("\nProduto inválido!")

                elif opcao_logado == "4" and usuario_atual[2] == "2":
                    print("\n--- AGENDAR RETIRADA ---")
                    data = input("Data para retirada (ex: 15/05): ")
                    hora = input("Horário (ex: 08:30): ")
                    carga = input("O que será retirado? ")
                    
                    agendamentos.append([login, data, hora, carga])
                    print(f"\nAgendamento realizado para {data} às {hora}!")

        else:
            print("\nLogin ou senha incorretos.")

    elif menu == "2":
        login = input("Login: ")
        senha = input("Senha: ")
        if login == "" or senha == "":
            print("\nErro: Login e senha não podem ser vazios.")
        else:
            print("\nNível de acesso:")
            print("1 - Administrador")
            print("2 - Cliente")
            tipo = input("Escolha: ")
            usuarios.append([login, senha, tipo])
            print(f"Usuário {login} cadastrado!")
    
    else:
        print("Opção inválida!")