# 04 Escreva  um  algoritmo  que  converta  centímetros  para  polegadas  (obs.:  1pol  = 2.54cm).

cent = float(input("Informe a quantidade em centimetros: "))

conv = cent / 2.54 

print(f'{cent} centimetros convertidos em polegadas é igual a:{conv:.2f} polegadas') 
# A estrutura "variável:.2f" faz com que só apareçam duas casas decimais após a virgula, o valor pode ser mudado de acordo com a vontade do programador
# variável:.nf -> variável:.5f