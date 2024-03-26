#1 –Faça um programa que receba três notas de um aluno, calcule sua média final e diga se o mesmo está aprovado ou reprovado (se sua média for maior que 5, estará aprovado

nts_lista =[]

for i in range(3):
    nts = float(input(f"Informe a {i + 1}° nota: "))
    nts_lista.append(nts)

s = sum(nts_lista)
md = s / 3

if md > 5:
    print(f"Aprovado com uma média igual a: {md:.2f}")
else:
    print(f"Reprovado com uma média igual a: {md:.2f}")