# Escreva um programa que receba as notas de cinco alunos em uma lista e calcule e exiba:
#•A   quantidade   de   alunos   com   nota   abaixo   de   5.0   e   os   informe   como "Reprovados";
#•A quantidade de alunos com nota entre 5.0 e 7.0 e os informe como "Final";
#•A quantidade de alunos com nota acima de 7.0 e os informe como "Aprovados";
#•A média das notas dos alunos.

notas = []

rep = []
fnl = []
apv = []

media = 0

for i in range(5):
    n = float(input("Informe a sua nota: "))
    notas.append(n)

for n in notas:
    if n < 5:
        rep.append(n)

for n in notas:
    if n == 5 or n <= 7:
        fnl.append(n)

for n in notas:
    if n >= 7:
        apv.append(n)

media = (sum(rep) + sum(fnl) + sum(fnl) ) / 3

print(f"A quantidade de alunos com nota acima de 7.0 é: {len(apv)} e eles estão aprovados")

print(f"A quantidade de alunos com nota abaixo de 5.0 é: {len(rep)} e eles estão reprovados")

print(f"A quantidade de alunos com nota entre 5.0 e 7.0 é: {len(fnl)} e eles estão na final")

print(f"A média de notas é: {media:.2f}")