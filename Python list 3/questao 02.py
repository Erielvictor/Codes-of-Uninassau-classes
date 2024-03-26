# 2 –Faça um programa que verifica a validade de uma senha fornecida pelo usuário. Se o usuário digitar a senha ‘123456’, escrever a mensagem ‘Acesso liberado’. Caso contrário, escrever ‘Acesso negado’.

senha = 123456

res = int(input("Informe a senha de acesso: "))

if res == senha:
    print("Acesso liberado!")
else:
    print("Acesso negado")