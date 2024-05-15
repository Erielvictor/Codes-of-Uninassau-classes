#Faça um programa que leia um número inteiro e o submeta para a função checaPositivo (crie a função), que deverá informar se o número digitado é positivo ou nega

n = int(input("Digite um número inteiro: "))

def checaPositivo(n):
    if n > 0:
        pos = n
        print(pos)
    else:
        print("O número é negativo")

checaPositivo(n)