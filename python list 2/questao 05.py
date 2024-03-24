# 05 Escreva um algoritmo para ler o raio de um círculo. Em seguida calcule e mostre a sua área: (A= πR2).

import math # importa a biblioteca de matemática, igual o portugol.

r = float(input("Informe o raio do círculo: "))


a =(3.14 * math.pow(r,2)) # math.pow() é um serviço que faz a POTENCIAÇÃO, precisa colocar a variável e o expoente.
# math.pow(var, expoente)

print(f"A área do círculo é igual a: {a:.2f}")
# A estrutura "variável:.2f" faz com que só apareçam duas casas decimais após a virgula, o valor pode ser mudado de acordo com a vontade do programador
# variável:.nf -> variável:.5f 
