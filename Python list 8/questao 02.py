# Faça um programa que lê 3 notas de um aluno no semestre, calcula sua média a partir de uma função e informa se o aluno está aprovado (media >= 7) ou reprovado (media < 7);

notas = []
media = 0

for i in range(3):
    n = float(input(f"Informe a sua {i + 1}°nota: "))
    notas.append(n)

media = sum(notas) / 3


if media >= 7:
    print("Aluno aprovado")
elif media < 7:
    print("Aluno reprovado")
else:
    print("Resultado inválido!")