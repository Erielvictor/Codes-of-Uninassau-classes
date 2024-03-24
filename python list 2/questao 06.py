# 06 Escreva um algoritmo que calcule e mostre a área e o volume de um cilindro (A = 2 π r(h+r),  V = π r2 h).

import math # importa a biblioteca de matemática, igual o portugol.
 
r = float(input("Informe o raio do cilindro: "))
h = float(input("Informe a altura do cilindro:  "))

pi = 3.14

area = 2 * pi * r*(h + r)
vol = pi * math.pow(r,2)* h # math.pow() é um serviço que faz a POTENCIAÇÃO, precisa colocar a variável e o expoente.
# math.pow(var, expoente)

print(f"A área do cilindro é igual a: {area:.2f}")
print(f"O volume do cilindro é igual a: {vol:.2f}")
# A estrutura "variável:.2f" faz com que só apareçam duas casas decimais após a virgula, o valor pode ser mudado de acordo com a vontade do programador
# variável:.nf -> variável:.5f