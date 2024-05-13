# Desenvolva  um  programa  que  receba  as  idades  de  cinco  pessoas  em  uma  lista  e determine e exiba:
#•A quantidade de pessoas com idade abaixo de 18 anos;
#•A quantidade de pessoas com idade entre 18 e 60 anos;
#•A quantidade de pessoas com idade acima de 60 anos;
#•A idade média das pessoas.

idade = []

jovem = []
adulto = []
idoso = []

media = 0

for i in range(5):
    n = int(input("Informe a sua idade: "))
    idade.append(n)

for n in idade:
    if n < 18:
        jovem.append(n)

for n in idade:
    if n >= 18 and n <= 60:
        adulto.append(n)

for n in idade:
    if n > 60:
        idoso.append(n)

media = (sum(jovem) + sum(idoso) + sum(adulto) ) / 3

print(f"A quantidade de pessoas com idade abaixo de 18 anos é: {len(jovem)}")

print(f"A quantidade de pessoas com idade entre 18 e 60 anos é: {len(adulto)}")

print(f"A quantidade de pessoas com idade acima de 60 anos é: {len(idoso)}")

print(f"A média de idades é: {media:.2f}")