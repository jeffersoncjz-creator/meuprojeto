
import auth as user
import animal as fa

fa.iniciarArquivo()

def iniciarMenuAnimais():
    while True:
        print('\n==================== MENU ANIMAIS ====================')
        print('1 - CADASTRAR ANIMAL')
        print('2 - BUSCAR ANIMAL POR BRINCO')
        print('3 - LISTAR ANIMAIS')
        print('4 - ALTERAR ANIMAL')
        print('5 - REMOVER ANIMAL')
        print('0 - Voltar ao Menu Inicial')
        print('======================================================')
        op = input("digite a opçao")
        if op == "1": fa.cadastrarAnimal()
        elif op == "2": fa.buscarAnimalPorBrinco()
        elif op == "3":fa.listarAnimais()
        elif op == "4":fa.alterarAnimal()
        elif op == "5":fa.apagarAnimal()
        elif op == "0":print("opção invalida")
    

while True:
    # MENU INICIAL (LOGIN / CADASTRO)
    print('\n======================')
    print('    FAZENDA SERTÃO    ') 
    print('======================')
    print('1 - Cadastrar usuário')
    print('2 - Login')
    print('0 - Sair')
    print('======================')

    while True:
        opcao = input('Digite a opção: ')
        if opcao in ['1', '2', '0']:
            break
        else:
            print('Opção inválida! Digite 1, 2 ou 0.\n')

    if opcao == '1':user.menu_user()
    elif opcao == '2':
        usuario = user.menu_user_login()
        print(usuario)
        if(usuario and usuario=="ADMINISTRADOR"):
            iniciarMenuAnimais()
            pass
        elif(usuario and usuario=="CLIENTE"):
            #menu_cliente()
            pass
        else:
            print("usuario não encontrado")
    elif opcao == '0':
        print('\nSistema encerrado. Até logo!')
        break    
            
        #     while True:
        #         iniciarMenuAnimais()
        #         opcao_animal = input('Digite a opção: ')
                
        #         if opcao_animal == '0':
        #             fa.salvarArquivo()
        #             print("\nDados dos animais salvos com sucesso!")
        #             break
        #         elif opcao_animal == '1':
        #             fa.cadastrarAnimal()
        #         elif opcao_animal == '2':
        #             brinco = input('Digite o brinco do animal: ')
        #             fa.buscarAnimalPorBrinco(brinco)
        #         elif opcao_animal == '3':
        #             fa.listarAnimais()
        #         elif opcao_animal == '4':
        #             brinco = input('Digite o brinco do animal que deseja alterar: ')
        #             fa.alterarAnimal(brinco)
        #         elif opcao_animal == '5':
        #             print('Para apagar informe o dado abaixo')
        #             brinco = input('Digite o brinco do animal que deseja apagar: ')
        #             fa.apagarAnimal(brinco)
        #         else:
        #             print('Opção inválida!')
        # else:
        #     print('\nUsuário ou senha incorretos.')


    