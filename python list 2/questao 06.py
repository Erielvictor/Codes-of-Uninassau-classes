# 06 Escreva um algoritmo que calcule e mostre a área e o volume de um cilindro (A = 2 π r(h+r),  V = π r2 h).

import math

r = float(input("Informe o raio do cilindro: "))
h = float(input("Informe a altura do cilindro:  "))

pi = 3.14

area = 2 * pi * r*(h + r)
vol = pi * math.pow(r,2)* h

print(f"A área do cilindro é igual a: {area:.2f}")
print(f"O volume do cilindro é igual a: {vol:.2f}")