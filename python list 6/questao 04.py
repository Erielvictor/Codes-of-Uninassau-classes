# Faça um programa que lê 4 números reais em uma lista, calcula e exibe a quantidade de números negativos e a soma dos números positivos dessa mesma

import math as mt

numeros = []
neg = []
pos = []

neg_quant = 0
pos_s = 0


for i in range(4):
    num = float(input(f"Informe o {i + 1}° número inteiro: "))
    numeros.append(num)
    

for num in numeros:
    if num >= 0:
        pos = num
        print(f"{pos}")
        

for num in numeros:
    if num < 0:
        neg.append(num)
        print(neg)
        neg_quant += 1
        print(neg_quant)


print(numeros)
print(neg)
print(pos)

