#Faça  um  programa  que  leia  o  raio  de  uma  esfera  e  submeta  os  dados  para  a  função volume (crie a função), que deverá calcular o seu volume;
#•V = 4/3 * (R*R*R)

r = float(input("Informe o raio da esfera: "))

def volume(r):
    v = (4/3) * (r ** 3)
    return v

vol = volume(r)

print(f"O volume da esfera é igual a: {vol:.2f}")