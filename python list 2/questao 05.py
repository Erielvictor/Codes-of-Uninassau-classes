# 05 Escreva um algoritmo para ler o raio de um círculo. Em seguida calcule e mostre a sua área: (A= πR2).

import math

r = float(input("Informe o raio do círculo: "))


a =(3.14 * math.pow(r,2))

print(f"A área do círculo é igual a: {a:.2f}")
