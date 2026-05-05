contatos = [
    ["Jeff", 8399177770, "jeff@email"], 
    ["Jose", 8383838383, "jose@email"], 
    ["Lucas", 8494848484, "lucas@email"],
    ["Ana", 914848484, "ana@email"],
]

while True:
    print("\nBem-Vindo a ContactPython App! By: Jeff")
    print("1 - Criar Contato")
    print("2 - Buscar Contato por nome")
    print("3 - Listar Contatos")
    print("4 - Alterar Contato")
    print("5 - Apagar contato")
    print("6 - Buscar Contato por numero")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")
    
    if opcao == "0":
        print("Saindo...")
        break
    elif opcao == "1":
        nome = input("Digite o nome do contato: ")
        celular = input("Digite o número do contato: ")
        email = input("Digite o e-mail do contato: ")
        contatos.append([nome, celular, email])
        print(f"Contato {nome} adicionado com sucesso!")
    elif opcao == "2":
        nome = input("Digite o nome do contato para buscar: ")
        encontrado = False
        for c in contatos:
            if c[0].lower() == nome.lower():
                print(f"{c[0]} | {c[1]} | {c[2]}")
                encontrado = True
                break
        if not encontrado:
            print("Contato não encontrado.")
    elif opcao == "3":
        print("-" * 50)
        for c in contatos:
            print(f"{c[0]} | {c[1]} | {c[2]}")
        print("-" * 50)
    elif opcao == "4":
        print("Para alterar informe o dado abaixo")
        celular = input("Digite o nome do contato: ")
        for posicao in range(len(contatos)):
            if contatos[posicao][1] == celular:
                nome = input("Digite o novo nome: ")
                celular = input("Digite o novo numero: ")
                email = input("Digite o novo email: ")
                contatos[posicao] = [nome, celular, email]
                print("\n\nContato alterado com sucesso!\n\n")
    elif opcao == "5":
        nome = input("Digite o nome do contato para apagar: ")
        encontrado = False
        for i, c in enumerate(contatos):
            if c[0].lower() == nome.lower():
                confirmacao = input(f"Tem certeza que deseja apagar {c[0]}? (s/n): ")
                if confirmacao.lower() == 's':
                    contatos.pop(i)
                    print("Contato apagado com sucesso!")
                else:
                    print("Operação cancelada!")
                encontrado = True
                break
        if not encontrado:
            print("Contato não encontrado.")
    elif opcao == "6":
        numero = input("Digite o número do contato para buscar: ")
        encontrado = False
        for c in contatos:
            if str(c[1]) == numero:
                print(f"{c[0]} | {c[1]} | {c[2]}")
                encontrado = True
                break
        if not encontrado:
            print("Contato não encontrado.")
    else:
        print("Opção inválida! Digite um número entre 0 e 6.")