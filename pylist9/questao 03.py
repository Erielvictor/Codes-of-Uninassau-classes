# Agenda telefônica (Cadastro) -Faça um programa que:
#•Receba o nome e o telefone de 3 pessoas;
#•Receba o nome do arquivo a ser criado;
#•Crie um arquivo (com o nome do arquivo indicado pelo usuário) para cada pessoa e #escreva o nome e o telefone no mesmo;
#oO nome deverá ficar na primeira linha do arquivo;
#oO telefone deverá ficar na segunda linha do arquivo

#from lib.defs import *
dados = []


def criarArq(nome_arq):
    try:
        a = open(nome_arq, 'wt+')
        a.close()
    except:
        print('Houve um error')
        nome_arq = str(input("Dê um nome ao arquivo: "))
        a = open(nome_arq, 'wt+')
        a.close()
    else:
        print('Arquivo Criado')
    return nome_arq

def cadastrar(nome_arq):
    arq = open(nome_arq, 'w')
    for i in range(3):
        nome = str(input("Informe o seu nome: "))
        #num = str(input("Informe o seu número: "))
        arq.write(f'{nome} \n')
    arq.close()

def mostrar(nome_arq):
    arq = open(nome_arq, 'r')
    dados = arq.readlines()
    print(dados[1])
    arq.close()

criarArq(nome_txt)
cadastrar(dados)
mostrar(dados)