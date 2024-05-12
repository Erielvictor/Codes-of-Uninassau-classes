#7 -Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificaçãoapós novo preço.
#% de aumento:
# até R$ 50 -> 5%
# entre 50 e 100 -> 10%
# classificação de aumento:
# até 80 reais -> barato
#entre 80 e 120(inclusi ve, <=) -> normal
#entre 120 e 200(inclusive, <=) .> caro
# maior que 200 -> caro

preco = float(input("Informe o valor do produto: R$ "))

if preco <= 50:
    nv_preco = preco +(preco * 0.05)

elif preco > 50 and preco <= 100:
    nv_preco = preco + (preco * 0.10)

elif preco > 100:
    mv_preco = preco + (preco * 0.15)

if nv_preco <= 80:
    print(f"A classificação do novo preço é: Barato. Sendo o valor final igual a: R$ {nv_preco}")

elif nv_preco > 80 and nv_preco <= 120:
    print(f"A classificação do novo preço é: Normal. Sendo o valor final igual a: R$ {nv_preco}")

elif nv_preco > 120 and nv_preco <= 200:
    print(f"A classificação do novo preço é: Caro. Sendo o valor final igual a: R$ {nv_preco}")

else:
    print(f"A classificação do novo preço é: Muito caro. Sendo o valor final igual a: R$ {nv_preco}")
