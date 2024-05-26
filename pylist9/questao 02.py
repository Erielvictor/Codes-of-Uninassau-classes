# Faça um programa que leia o nome de 3 pessoas, 
#cadastrando-as em um arquivo. 
#Em seguida, o programa deverá exibir apenas o nome da 2 pessoa cadastra

arq = 'nomes.txt'
dados = []

def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um error')
        nome = str(input("Dê um nome ao arquivo: "))
        a = open(nome, 'wt+')
        a.close()
    else:
        print('Arquivo Criado') 


def cadastrar(nome):
    arq = open('nomes.txt', 'a')
    
    for i in range(3):
        nome = str(input("Informe o seu nome: "))
        arq.write((nome) + '\n')
    arq.close()

def mostrar(dados):
    arq = open('nomes.txt', 'r')
    dados = arq.readlines()
    print(dados[1])
    arq.close()


criarArq(arq)
cadastrar(arq)
mostrar(dados)