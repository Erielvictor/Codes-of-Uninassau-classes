# Faça  um  programa  que  receba  6  números  inteiros  em  uma  lista  e  mostra  apenas  os números positivos

lista = []
pos = []

for i in range(4):
    res = int(input(f"Informe o {i + 1}° número inteiro: "))
    lista.append(res)

for res in lista:
    if res >= 0:
        pos = res
        print(f"[{pos}]")
    