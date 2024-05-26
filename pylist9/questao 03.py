# Agenda telefônica (Cadastro) -Faça um programa que:
#•Receba o nome e o telefone de 3 pessoas;
#•Receba o nome do arquivo a ser criado;
#•Crie um arquivo (com o nome do arquivo indicado pelo usuário) para cada pessoa e #escreva o nome e o telefone no mesmo;
#oO nome deverá ficar na primeira linha do arquivo;
#oO telefone deverá ficar na segunda linha do arquivo

from lib.defs import *

arq = ''
user = []


cadastro()
mostrar()
if not arqExist(arq):
    print('O arquivo não existe')
    criarArq(arq)
else:
    print("O arquivo existe")