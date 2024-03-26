#3 -Faça um programa que lê o número de gols marcados pelo Sport e o número de gols marcados pelo Náutico. Escrever o nome do time vencedor. Caso não haja vencedor, escrever EMPATE.

g_Sport = int(input("Informe a quantidade de gols marcados pelo Sport:  "))
g_nau = int(input("Informe a quantidade de gols marcados pelo Náutico:  "))

if g_Sport > g_nau:
    print("O Sport venceu a partida!")
elif g_nau > g_Sport:
    print("O Náutico venceu a partida!")
else:
    print("Empate!")