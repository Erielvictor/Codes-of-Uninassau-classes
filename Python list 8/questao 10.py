# Faça um programa que receba dois números e execute as operações listadas a seguir, de acordo com a escolha do usuário (crie uma função para cada opç

def media(n1, n2):
    res = (n1 + n2) / 2 
    return res

def dif(n1, n2):
    if op == 2:
        if n1 > n2:
            res = n1 - n2
        elif n2 > n1:
            res = n2 - n1
        else:
            return "Operação inválida"
    return res

def pro(n1, n2):
    res = n1 * n2
    return res

def div(n1, n2):
    if n2 != 0:
        res = n1 / n2
    else:
        return "Error"
    return res


n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um outro número inteiro: "))

print("Operações: \n [1] adição \n [2] subtração \n [3] multiplicação \n [4] divisão")

op = int(input("Informe a operação desejada: "))

if op == 1:
    res = media(n1, n2)
    print(f"A média dos números é: {res}")
elif op == 2:
    res = dif(n1, n2)
    print(f"A diferença entre os números é: {res}")
elif op == 3:
    res = pro(n1, n2)
    print(f"O resultado do produto dos números é: {res}")
elif op ==4:
    res = div(n1, n2)
    print(f"O resultado da divisão dos números é: {res}")
else:
    print("Operação inválida!")