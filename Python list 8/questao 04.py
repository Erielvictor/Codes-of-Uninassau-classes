#Faça  um  programa  que  lê  o  preço  de  um  produto  e  a  quantidade  adquirida  por  um cliente.
# O mesmo deverá calcular, a partir de uma função, o valor total a ser pago pelo cliente;
def calcular_vt(price, quant):
    valor_total = price * quant
    return valor_total

price = float(input("Informe o preço do produto:R$ "))
quant = int(input("Informe a quantidade adquirida: "))

valor_final = calcular_vt(price, quant)

print(f"O total da sua compra é: R${valor_final:.2f}")