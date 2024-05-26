def linha(tam = 42):
    return "-" * 42

def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())


def cadastro(arq, user = '', num = 0):
    arq = open('dados.txt', 'w')

    user = str(input("Informe o nome usuário: "))
    arq.write(user)
    
    arq.close