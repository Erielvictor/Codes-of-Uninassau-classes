# Faça um programa que leia a variação da distância percorrida por um carro e a variação de  tempo  que  ele  levou  para  percorrer  o  trajeto  e  calcula,  a  partir  de  uma  função,  a velocidade média do veículo;
#•Velocidade media = (Km final –km inicial) / (hora final –hora inicial)

d_i = float(input("Informe a distância inicial[km]: "))
d_f = float(input("Informe a distância final[km]: "))

h_i = float(input("Informe a hora inicial em horas: "))
h_f = float(input("Informe a hora final em horas: "))

vm = (d_f - d_i) / (h_f - h_i)

print(f"{vm} km/h")

#def vm(a, b, c, d):
    