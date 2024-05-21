# Faça um programa que cadastre a senha de 4 usuários em uma matriz 2x2. Em seguida, o  programa  deverá  solicitar  ao  usuário  sua  senha.  Caso  a  senha  digitada  esteja cadastrada na matriz de senhas, o programa deverá exibir a mensagem “Bem vindo!”. Caso contrário, deverá exibir a frase “Usuário não cadastrada"

senhas = [["" for _ in range(2)] for _ in range(2)]
for i in range(2):
    for j in range(2):
        senhas[i][j] = input(f"Cadastre a senha do usuário na posição ({i+1},{j+1}): ")

senha_dig = input("Digite sua senha: ")

senha_encontrada = False
for i in range(2):
    for j in range(2):
        if senhas[i][j] == senha_dig:
            senha_encontrada = True
            break

if senha_encontrada:
    print("Bem vindo!")
else:
    print("Usuário não cadastrado")