salario = float(input()) #Jean-Lucas Luquetti Silva / RA: 120443
if (salario < 1800):
    salario = (salario * 1.255) #caso o salário seja menor que 1,800R$, terá reajuste de 25,5%
else :
    salario = (salario * 1.1225) #acima, terá reajuste de 12,25%
print('{:.4f}'.format(salario))