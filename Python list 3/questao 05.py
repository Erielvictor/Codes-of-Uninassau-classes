# 5 -Faça  um  programa  que  receba  dois  números  e  execute  as  operações  listadas  a  seguir,  de acordo com a escolha do usuário.

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

res = 0

while res != 5:
    print("[1] média \n"
      "[2] subtração\n"
      "[3] multiplicação\n"
      "[4] Divisão\n"
      "[5] Encerrar\n")
    res = int(input("Informe a sua escolha: "))

    if res == 1:
        med = (n1 + n2) / 2
        print(med)

    elif res == 2:
        sub = n1 - n2
        print(sub)
    
    elif res == 3:
        mult = n1 * n2
        print(mult)

    elif res == 4:
        div = n1 / n2
        print(div)

    elif res == 5:
        print("Finalizando")
