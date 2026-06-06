

with open("atualizacaov2/arquivos/usuarios.txt", "a", encoding="utf-8") as arquivo:
    pass

def cadastrausuario(login, senha, tipo):
    with open("atualizacaov2/arquivos/usuarios.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            if len(dados) == 3 and dados[0] == login:
                return False

    with open("atualizacaov2/arquivos/usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{login};{senha};{tipo}\n")
    return True


def login(login, senha):
    with open("atualizacaov2/arquivos/usuarios.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(';')
            if len(dados) == 3 and dados[0] == login and dados[1] == senha:
                return dados[2]
                
    return None 


def menu_user_cadastrar():
    nome = input('Digite o usuário: ')
    senha = input('Digite a senha: ')
    
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

def menu_user_login():
    nome = input('Usuário: ')
    senha = input('Senha: ')
    
    usuario = login(nome, senha)
    
    if usuario:
        funcao = "ADMINISTRADOR" if usuario == "1" else "CLIENTE"
        print(f'\nBem-vindo, {nome}! Você está logado com sucesso como {funcao}!')
        return funcao
    else:
        return None