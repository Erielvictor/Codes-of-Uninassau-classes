#Faça um programa que receba o preço de cinco produtos em uma lista, calcula e exiba:•
#A quantidade de produtos com preço inferior a R$ 50,00;
#•A quantidade de produtos com preço entre R$ 50,00 e 80,00;
#•A quantidade de produtos com preço acima de R$ 80,00
#•A média de preço dos produtos;

prod = []

A = []
B = []
C = []

A_quant = 0
B_quant = 0
C_quant = 0


media = 0

for i in range(5):
    p = float(input(f"Informe o preço do {i + 1}° produto:  "))
    prod.append(p)

for p in prod:
    if p < 50:
        A.append(p)
        A_quant = A_quant + 1

for p in prod:
    if p >= 50 and p <= 80:
        B.append(p)
        B_quant = B_quant + 1

for p in prod:
    if p > 80:
        C.append(p)
        C_quant = C_quant + 1

media = (sum(A) + sum(B) + sum(C)) / 3

print(f"A quantidade de produtos com preço inferior a R$ 50,00 é igual a: {A_quant}")

print(f"A quantidade de produtos com preço entre R$ 50,00 e 80,00 é igual a: {B_quant}")

print(f"A quantidade de produtos com preço acima de R$ 80,00 é igual a: {C_quant}")

print(f"A média dos preços é igual a: R$ {media:.2f}")