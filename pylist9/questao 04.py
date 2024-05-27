#4-Com base na questão anterior, faça um programa que faça LISTAGEM da Agenda telefônica, seguindo os seguintes passos:
#•Receba o nome do arquivo a ser lido;
#•Leia o arquivo indicado pelo usuário (a partir do nome do arquivo);
#•Exiba o nome e o telefone cadastrados no mesmo


nome_arq = input("Digite o nome do arquivo: ")

def cadastrar():
    arq = open(f'{nome_arq}.txt', 'w')
    lista_nomes = []
    lista_tel = []


    for i in range(3):
        nome = str(input("Informe o seu nome: "))
        num = str(input("Informe o seu número: "))
        lista_nomes.append(nome)
        lista_tel.append(num)
    for i in range(3):
        arq.write(f'{lista_nomes[i]} ')
    arq.write('\n')

    for i in range(3):
        arq.write(f"{lista_tel[i]} ")
    arq.close()

def mostrar():
    arq = open(f'{nome_arq}.txt', 'r')
    dados = arq.read()

    infos = dados.split('\n')

    if infos[-1] == '': 
        del infos[-1]
    
    nomes = infos[0].split()
    tel = infos[1].split()
    

    for i in range(len(nomes)):
        print(f'Pessoa {nomes[i]}, Telefone{tel[i]}')

cadastrar()
mostrar()