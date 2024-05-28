#Apenas um scrip pra armazenar algumas funções de teste.

def linha(tam = 42):
    return "-" * 42

def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())



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

def arqExist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastro():
    user = open('dados.txt', 'w')
    number = open('Tel.txt', 'w')
    for i in range(3):
        nome = str(input(f"Informe o nome do {i + 1}° cliente: "))
        num = str(input(f"Informe o número do {i + 1}° cliente: "))
        user.write(nome +  num +'\t'+ '\n')
        #number.write(num + '\n')
    user.close()
    #number.close()

def mostrar():
    user = open('dados.txt', 'r')
    number = open('Tel.txt', 'r')
    nomes = user.read()
    numeros = number.read()
    print(nomes)
    print(numeros)
    user.close()
    number.close()

