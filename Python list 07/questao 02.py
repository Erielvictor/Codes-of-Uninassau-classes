# Faça um programa que armazena valores inteiros em uma matriz 2x3. A seguir, calcula e exibe a soma dos valores positivos contidos na matriz


matriz = [[0, 0, 0], [0, 0, 0]]

soma_pos = 0

for i in range(2):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor inteiro: "))

for i in range(2):
    for j in range(3):
        if matriz[i][j] > 0:
            soma_pos += matriz[i][j]

# Exibindo o resultado
print(f"A soma dos valores positivos é: {soma_pos}")