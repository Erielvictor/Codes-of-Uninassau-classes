#Faça um programa que leia três inteiros que representam horas, minutos e segundos e submeta os dados para a função converte (crie a função), que deverá converter os três inteiros digitados para segundos (Ex.: 2h 40min e 10s correspondem a 9.610 segundos

def converter(h, m, s):
    t_s = (h * 3600) + (m * 60) + s
    return t_s

h = int(input("Informe a quantidade de horas: "))
m = int(input("Informe a quantidade de minutos: "))
s = int(input("Informe a quantidade de segundos: "))

t_s = converter(h, m, s)

print(f"O total de segundos é: {t_s} segundos")