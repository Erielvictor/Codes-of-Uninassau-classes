#Faça  um  programa  que  leia  dois  números  reais  e  um  símbolo  que  identifique  uma operação  matemática  (+, -,  *,  /),  submetendo-os  para  a  função  calculadora  (crie  a função). 
# A  função  deverá  efetuar  um  cálculo  entre  os  dois  números  submetidos, baseado no símbolodigitado;


def calculadora(n1, n2, op):
    if op == "+":
        res = n1 + n2 
    elif op == "-":
        res = n1 - n2
    elif op == "*":
        res = n1 * n2
    elif op == "/":
        if n1 == 0 or n2 == 0:
            print("ERROR: Divisão por zero!")
        else:
            res = n1 / n2
    else:
        return "operação inválida!"
    return res

while op != "E": 
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite um outro número inteiro: "))

    print("Operações: \n [+] adição \n [-] subtração \n [*] multiplicação \n [/] divisão")

    op = input("Informe a operação desejada: ")


    res_cal = calculadora(n1, n2, op)

    print(f"O resultado da operação é: {res_cal}")
        