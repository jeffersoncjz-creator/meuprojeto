
usuarios = []


while True:
    print("\n" + "="*40)
    print("\nBem-Vindo ao App Fazenda Sertão!\n ")
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
        if login == "" or senha == "":
                print("\nOpção inválida! Digite um valor.")

        for i in usuarios:
            if i[0] == login and i[1] == senha:
                encontrado = True
                print("Login realizado com sucesso!")
            

                print("\n=-=-=-=-MENU=-=-=-=-=")
                print(f"Bem vindo, {login}!\n")
        if not encontrado:    
            print("Contato não encontrado.")
            

    elif menu == "2":
        login = input("Login: ")
        senha = input("Senha: ")
        if login == "" or senha == "":
            print("\nOpção inválida! Digite um valor.")
        else:
            print("\nDefina o nivel de acesso do usuario! ")
            tipo = input("1 - Administrador ou 2 - Cliente ")
            usuarios.append([login, senha, tipo])
            if tipo == "1":
                print("Cadastrado como ADM!")
            elif tipo == "2":
                print("Cadastrado como Cliente!")
            else:
                print("Opção inválida")
    else:
        print("Opção inválida")



