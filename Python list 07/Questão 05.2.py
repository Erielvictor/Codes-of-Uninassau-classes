#Faça um programa que cadastre a senha de 4 usuários em uma matriz 2x2. Em seguida, o  programa  deverá  solicitar  ao  usuário  sua  senha.  Caso  a  senha  digitada  esteja cadastrada na matriz de senhas, o programa deverá exibir a mensagem “Bem vindo!”. Caso contrário, deverá exibir a frase “Usuário não cadastrado”

senhas_cad = [[0,0], [0,0]]

senha_encontrada = False



for i in range(2):
    for j in range(2):
        senhas_cad[i][j] = int(input("Informe a sua senha: "))

login = int(input("Informe a senha de login: "))


for i in range(2):
    for j in range(2):
        if senhas_cad[i][j] == login:
            senha_encontrada = True

if senha_encontrada:
    print("Bem vindo!")
else:
    print("Usuário não cadastrado!")


