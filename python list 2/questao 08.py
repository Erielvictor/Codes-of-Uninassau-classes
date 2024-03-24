# 08 Escreva  um  algoritmo que  leia  3  números  inteiros  e  mostre  os valores  em ordem crescente.

ordem = []

for i in range(3):
    num = int(input(f"Informe o {i + 1}° número: "))
    ordem.append(num)
    ord_new = sorted(ordem)

print(f"Os valores em ordem crescente são: {ord_new}")