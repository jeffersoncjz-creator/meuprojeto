import bcrypt

ARQUIVO_USUARIOS = "atualizacaov2/arquivos/usuarios.txt"


with open(ARQUIVO_USUARIOS, "a", encoding="utf-8"):
    pass


def cadastrausuario(login, senha, tipo):

    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(';')

            if len(dados) == 3 and dados[0] == login:
                return False

    senha_hash = bcrypt.hashpw(
        senha.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')

    with open(ARQUIVO_USUARIOS, "a", encoding="utf-8") as arquivo:

        arquivo.write(
            f"{login};{senha_hash};{tipo}\n"
        )

    return True


def login(login_usuario, senha):

    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:

        for linha in arquivo:

            dados = linha.strip().split(';')

            if len(dados) != 3:
                continue

            usuario = dados[0]
            senha_salva = dados[1]
            tipo = dados[2]

            if usuario == login_usuario:

                try:

                    if bcrypt.checkpw(
                        senha.encode('utf-8'),
                        senha_salva.encode('utf-8')
                    ):
                        return tipo

                except ValueError:

                    continue

    return None


def menu_user_cadastrar():

    print('\n====== CADASTRO DE USUÁRIO ======')

    nome = input('Digite o usuário: ').strip().lower()
    senha = input('Digite a senha: ').strip()

    while True:

        tipo = input(
            'Tipo (1 - ADMINISTRADOR | 2 - CLIENTE): '
        ).strip()

        if tipo in ['1', '2']:
            break

        print('Tipo inválido! Digite apenas 1 ou 2.\n')

    sucesso = cadastrausuario(
        nome,
        senha,
        tipo
    )

    if sucesso:
        print('\nUsuário cadastrado com sucesso!')
    else:
        print(
            '\nEste nome de usuário já está cadastrado.'
        )


def menu_user_login():

    print('\n======== LOGIN ========')

    nome = input('Usuário: ').strip().lower()
    senha = input('Senha: ').strip()

    usuario = login(
        nome,
        senha
    )

    if usuario:

        funcao = (
            "ADMINISTRADOR"
            if usuario == "1"
            else "CLIENTE"
        )

        print(
            f'\nBem-vindo, {nome}! '
            f'Você está logado como {funcao}.'
        )

        return {
            "nome": nome,
            "tipo": funcao
        }

    return None