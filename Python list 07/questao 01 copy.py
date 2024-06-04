#Faça um programa que  lê a altura de  4 pessoas em uma matriz 2x2, calcula e exibe a quantidade de pessoas com altura superior a 1.50 metros.


alturas = [[0,0], [0,0]]

maior = 0

for i in range(2):
    for j in range(2):
        alturas[i][j] = float(input("Informe a altura em centimetros[ex: 150]: "))

for i in range(2):
    for j in range(2):
        if alturas[i][j] > 150 and alturas[i][j] > 1.50:
            maior += 1

print(f"A quantidade de pessoas com altura superior a 1.50m é igual a: {maior}")

print(f"As alturas fornecidas foram: {alturas}")

