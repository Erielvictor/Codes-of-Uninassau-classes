# 01 Escreva  um  algoritmo que  leia  um valor e  determine  se  o valor  lido  e positivo  ou negativo.

n = int(input("Informe um número: "))

if n < 0:
    print("É negativo")
elif n > 0:
    print("É positivo")
else:
    print("Seu número é zero")