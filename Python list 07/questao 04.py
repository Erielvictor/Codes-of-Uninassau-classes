# Faça  um  programa  que  receba  o  nome  de  9  produtos  em  uma  matriz  3x3.  Logo  em seguida,  o  programa  deverá  solicitar  ao  usuário  a  linha  e  a  coluna  do  produto  a  ser acessado, imprimindo seu nome

prod = [["" for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        prod[i][j] = input(f"Digite o nome do produto na posição ({i+1},{j+1}): ")

linha = int(input("Digite a linha do produto que deseja acessar (1-3): ")) - 1
coluna = int(input("Digite a coluna do produto que deseja acessar (1-3): ")) - 1

if 0 <= linha < 3 and 0 <= coluna < 3:
    print(f"O produto na posição ({linha+1},{coluna+1}) é: {prod[linha][coluna]}")
else:
    print("Linha ou coluna inválida. Por favor, digite valores entre 1 e 3.")
