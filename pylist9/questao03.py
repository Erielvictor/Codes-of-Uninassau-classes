# Agenda telefônica (Cadastro) -Faça um programa que:
#•Receba o nome e o telefone de 3 pessoas;
#•Receba o nome do arquivo a ser criado;
#•Crie um arquivo (com o nome do arquivo indicado pelo usuário) para cada pessoa e #escreva o nome e o telefone no mesmo;
#oO nome deverá ficar na primeira linha do arquivo;
#oO telefone deverá ficar na segunda linha do arquivo

dados = []

nome_arq = input("Digite o nome do arquivo: ")


def cadastrar():
    arq = open(f'{nome_arq}.txt', 'w')
    for i in range(3):
        nome = str(input("Informe o seu nome: "))
        num = str(input("Informe o seu número: "))
        arq.write(f'{nome} \n {num}\n')
    arq.close()

cadastrar()
