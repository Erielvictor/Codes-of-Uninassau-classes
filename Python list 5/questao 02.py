# Faça um programa que recebe o preço de 10 produtos e exibe o valor do produto mais caro.

name_prod = []
price_prod = []

for i in range(10):
    
    n_prod = input("Informe o nome do produto: ")
    print(n_prod)
    name_prod.append(n_prod)

    p_prod = float(input("Informe o preço do produto: "))
    print(p_prod)
    price_prod.append(p_prod)
    zip(name_prod, price_prod)

expensive = max(price_prod)

print(f" O produto mais caro custa: {expensive}")

