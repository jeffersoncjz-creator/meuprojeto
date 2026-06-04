

animais = []

# funções da lista de animais
def cadastrarAnimal():
    print('\n--- CADASTRO DE ANIMAL ---')
    brinco = input('Digite o brinco: ')
    
    for a in animais:
        if a['brinco'] == brinco:
            print(f'\nO brinco "{brinco}" já está cadastrado para o animal "{a["nome"]}".')
            print('Cadastro cancelado!\n')
            return
            
    nome = input('Digite o nome do animal: ')
    valor = input('Digite o valor: ')
    
    novo_animal = {"nome": nome, "brinco": brinco, "valor": valor}
    animais.append(novo_animal)
    print('\nAnimal cadastrado com sucesso!\n')

def buscarAnimalPorNome(nome):
    print('-' * 50)
    for a in animais:
        if a['nome'] == nome:
            print(a['nome'], ' | ', a['brinco'], ' | ', a['valor']) 
    print('-' * 50)

def buscarAnimalPorBrinco(brinco):
    print('-' * 50)
    for a in animais:
        if a['brinco'] == brinco:
            print(a['nome'], ' | ', a['brinco'], ' | ', a['valor']) 
    print('-' * 50)

def listarAnimais():
    print('-' * 50)
    for a in animais:
        print(a['nome'], ' | ', a['brinco'], ' | ', a['valor']) 
    print('-' * 50)

def alterarAnimal(brinco):
    print('Para alterar informe o dado abaixo')
    for posicao in range(len(animais)):
        if animais[posicao]['brinco'] == brinco:
            nome = input('Digite o novo nome: ')
            brinco_novo = input('Digite o novo brinco: ')
            
            # Validação extra opcional: Se ele mudar o brinco, checa se o novo brinco já não existe em OUTRO animal
            if brinco_novo != brinco:
                for a in animais:
                    if a['brinco'] == brinco_novo:
                        print(f'\nO brinco "{brinco_novo}" já pertence a outro animal. Alteração cancelada!\n')
                        return

            valor = input('Digite o novo valor: ')
            a = {"nome": nome, "brinco": brinco_novo, "valor": valor}
    
            animais[posicao] = a
            print('\n\nAnimal alterado com sucesso!\n\n')
            return
    print('Animal não encontrado!')

def apagarAnimal(brinco):
    for posicao in range(len(animais)):
        if animais[posicao]['brinco'] == brinco:
            animais.pop(posicao)
            print('Animal removido com sucesso!')
            break

def salvarArquivo():
    with open("atualizacaov2/arquivos/animais.txt", "w", encoding="utf-8") as arq:
        for a in animais:
            arq.write(f'{a["nome"]},{a["brinco"]},{a["valor"]}\n')

def iniciarArquivo():
    try:
        with open("atualizacaov2/arquivos/animais.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
            for c in conteudo:
                c = c.replace('\n', '')
                dados = c.split(',')
                if len(dados) >= 3:
                    nome = dados[0]
                    brinco = dados[1]
                    valor = dados[2]
                    animais.append({
                        "nome": nome,
                        "brinco": brinco,
                        "valor": valor
                    })
    except FileNotFoundError:
        with open("atualizacaov2/arquivos/animais.txt", "w", encoding="utf-8") as arquivo:
            pass