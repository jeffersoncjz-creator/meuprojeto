

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