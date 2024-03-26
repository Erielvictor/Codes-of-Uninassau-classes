# 4 -Faça um programa que leia três valores inteiros A, B e C e diga se a soma de A + B é menor que C.

a = int(input("Informe um valor inteiro: "))
b = int(input("Informe um valor inteiro: "))
c = int(input("Informe um valor inteiro: "))

if a + b < c:
    print("A soma entre A e B é menor que C")
else:
    print("A soma entre A e B é maior que C")