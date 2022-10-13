valor = int(input()) #Jean-Lucas Luquetti Silva / RA: 120443
aux = 1 #Auxiliar de contagem
soma = 0 #Contador da soma dos divisores positivos
while (aux < valor): #Criação de um laço pra somar divisores positivos
	if ((valor % aux) == 0):
		soma = soma + aux
		aux = aux + 1
	else :
		aux = aux + 1
if (soma == valor):
	print('sim')
else :
	print('nao') 