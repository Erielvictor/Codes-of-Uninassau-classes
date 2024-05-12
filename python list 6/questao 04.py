# Faça um programa que lê 4 números reais em uma lista, calcula e exibe a quantidade de números negativos e a soma dos números positivos dessa mesma

numeros = []
#neg = []
pos = []

neg_quant = 0
pos_s = 0


for i in range(4):
    num = int(input(f"Informe o {i + 1}° número inteiro: "))
    numeros.append(num)

for num in numeros:
    if num < 0:
        #neg = numeros
        #print(neg)
        neg_quant = neg_quant + 1
        print(neg_quant)


for num in numeros:
    if num > 0:
        pos += num

pos_s =sum(pos)
print(pos_s)

