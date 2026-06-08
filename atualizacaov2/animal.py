from tabulate import tabulate
import csv
import os

ARQUIVO_VENDAS = "atualizacaov2/arquivos/vendas.csv"



animais = []

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

    tabela = []

    for a in animais:

        if a['nome'].lower() == nome.lower():

            tabela.append([
                a['brinco'],
                a['nome'],
                f"R$ {float(a['valor']):.2f}"
            ])

    if not tabela:

        print("\nAnimal não encontrado.\n")
        return

    print(
        tabulate(
            tabela,
            headers=[
                "Brinco",
                "Nome",
                "Valor"
            ],
            tablefmt="grid"
        )
    )

def buscarAnimalPorBrinco(brinco):

    tabela = []

    for a in animais:

        if a['brinco'] == brinco:

            tabela.append([
                a['brinco'],
                a['nome'],
                f"R$ {float(a['valor']):.2f}"
            ])

    if not tabela:

        print("\nAnimal não encontrado.\n")
        return

    print(
        tabulate(
            tabela,
            headers=[
                "Brinco",
                "Nome",
                "Valor"
            ],
            tablefmt="grid"
        )
    )

def listarAnimais():

    if not animais:
        print("\nNenhum animal cadastrado.\n")
        return

    tabela = []

    for a in animais:

        tabela.append([
            a['brinco'],
            a['nome'],
            f"R$ {float(a['valor']):.2f}"
        ])

    print("\nANIMAIS CADASTRADOS\n")

    print(
        tabulate(
            tabela,
            headers=[
                "Brinco",
                "Nome",
                "Valor"
            ],
            tablefmt="grid"
        )
    )

def alterarAnimal(brinco):

    listarAnimais()

    print('\nPara alterar informe os novos dados:')
    for posicao in range(len(animais)):
        if animais[posicao]['brinco'] == brinco:
            nome = input('Digite o novo nome: ')
            brinco_novo = input('Digite o novo brinco: ')
            
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

def comprarAnimal(nome_cliente):
    print('\n--- COMPRA DE ANIMAL ---')

    listarAnimais()

    brinco = input(
    '\nDigite o brinco do animal que deseja comprar: '
).strip()
    

    for posicao in range(len(animais)):
        if animais[posicao]['brinco'] == brinco:
            
            animal_comprado = animais.pop(posicao)
            
            arquivo_existe = os.path.exists(ARQUIVO_VENDAS)
            with open(ARQUIVO_VENDAS, "a", newline="", encoding="utf-8") as arquivo:

                escritor = csv.writer(arquivo)

            if not arquivo_existe:

                escritor.writerow([
                    "tipo",
                    "cliente",
                    "item",
                    "quantidade",
                    "valor"
                ])

            escritor.writerow([
                "ANIMAL",
                nome_cliente,
                animal_comprado["nome"],
                1,
                animal_comprado["valor"]
            ])
            
            print(f"\nCompra realizada com sucesso para o cliente: {nome_cliente}!")
            print(f"Animal: {animal_comprado['nome']} | Valor: R$ {animal_comprado['valor']}\n")
            
            nome_extrato = f"atualizacaov2/arquivos/extrato_{nome_cliente}.txt"
            with open(nome_extrato, "a", encoding="utf-8") as extrato:
                extrato.write("="*40 + "\n")
                extrato.write("          EXTRATO DE COMPRA          \n")
                extrato.write("="*40 + "\n")
                extrato.write(f"Cliente: {nome_cliente}\n")
                extrato.write(f"Item: {animal_comprado['nome']} (Animal)\n")
                extrato.write(f"Brinco: {animal_comprado['brinco']}\n")
                extrato.write(f"Valor Pago: R$ {animal_comprado['valor']}\n")
                extrato.write("="*40 + "\n\n")
            
            print(f"Extrato atualizado em: {nome_extrato}")
            
            salvarArquivo()
            return
            
    print('Animal não encontrado com este brinco!')



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