# Faça  um  programa  que  lê  6  números  reais  em  uma  matriz  3x2,  calcula  e  exibe  a quantidade de números negativos e a soma dos números positivos dessa mesma

matriz = [[0, 0], [0, 0], [0, 0]]

quant_neg = 0
s_pos = 0.0

for i in range(3):
    for j in range(2):
        matriz[i][j] = float(input(f"Digite o número real na posição ({i+1},{j+1}): "))


for i in range(3):
    for j in range(2):
        if matriz[i][j] < 0:
            quant_neg += 1
        elif matriz[i][j] > 0:
            s_pos += matriz[i][j]

# Exibindo os resultados
print(f"Quantidade de números negativos: {quant_neg}")
print(f"Soma dos números positivos: {s_pos}")