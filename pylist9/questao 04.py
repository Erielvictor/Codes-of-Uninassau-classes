#4-Com base na questão anterior, faça um programa quefaça LISTAGEM da Agenda telefônica, seguindo os seguintes passos:
#•Receba o nome do arquivo a ser lido;•Leia o arquivo indicado pelo usuário (a partir do nome do arquivo);
#•Exiba o nome e o telefone cadastrados no mesmo


dados = []

nome_arq = input("Digite o nome do arquivo: ")

def cadastrar():
    arq = open(f'{nome_arq}.txt', 'w')
    for i in range(3):
        nome = str(input("Informe o seu nome: "))
        num = str(input("Informe o seu número: "))
        arq.write(f'{nome} \n {num}\n')
    arq.close()

def mostrar():
    arq = open(f'{nome_arq}.txt', 'r')
    dados = arq.read()

    infos = dados.split('\n')

    nomes = infos[0].split()
    tel = infos[1].split()
    for i in range(len(nomes)):
        print(f'Pessoa {nomes[i]}, Telefone{tel[i]}')

cadastrar()
mostrar()