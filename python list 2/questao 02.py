# 02 Escreva  um  algoritmo  que  leia  um  número  e  mostre  o  seu  antecessor  e  o  seu sucessor.

n = int(input("Informe um número: "))

ant = n - 1 # faz o cálculo de subtração. Como o antecessor é o número anterior então podemos colocar na forma matemática: ant = n - 1
suc = n + 1 # faz o cálculo de Adição. Como o sucessor é o número seguinte então podemos colocar na forma matemática: ant = n + 1

print(f'O antecessor do número {n} é: {ant} e o seu sucessor é: {suc}')