
senhas_cad = [[0,0], [0,0]]
cad_True = False

def cadastrar():
    arq = open(f"{nome}.txt", 'w')
    for i in range(2):
        for j in range(2):
            senhas_cad[i][j] = int(input(f"Informe a senha: "))
            arq.close()

    for i in range(2):
        for j in range(2):
            arq = open(f"{nome}.txt", 'w')
            arq.write(f"{senhas_cad}")
        arq.write("\n")
        arq.close()


def verificar():
    arq = open(f"{nome}.txt", 'r').read()
    login = int(input("Informe o login: "))
    for i in range(2):
        for j in range(2):
            if login == senhas_cad[i][j]:
                cad_True = True
            else: 
                cad_True = False
    if cad_True:
        print("Bem-vindo!")
    else:
        print("Senha não cadastrada.")        

nome = str(input("Informe o nome do arquivo: "))

cadastrar()
verificar()