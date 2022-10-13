import math
valor = float(input()) #Jean-Lucas Luquetti Silva / RA: 120443
if (valor >= 0): #determinar se o número é positivo
	valor = math.sqrt(valor) #utilizando-se da função da raíz quadrada
	print('{:.4f}'.format(valor))
else :
	valor = math.pow(valor, 2)
	print('{:.4f}'.format(valor))