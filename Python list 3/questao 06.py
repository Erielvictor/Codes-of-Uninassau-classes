# 6 -Faça um programa que calcula e exibe o salário reajustado de um funcionário. O percentual de aumento encontra-se na tabela a seguir.
# até 300 reais -> aumento de 35%
# Acima de 300 reais -> aumento de 15%

sal = float(input("Informe o seu salário em R$: "))

if sal <= 300:
    sal_novo = sal + (sal * (35/100))
    print(f"O seu salário novo é igual a: {sal_novo}")

elif sal > 300:
    sal_novo = sal + (sal * (15/100))
    print(f"O seu salário novo é igual a: {sal_novo}")