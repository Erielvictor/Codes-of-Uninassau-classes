#Faça  um  programa  que  leia  dois  números  inteiros  e  informa,  a  partir  de  uma  função, qual o maior número digitadop

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

def maior(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

maior_n = maior(n1, n2)

print(f"O maior número digitado é: {maior_n}")