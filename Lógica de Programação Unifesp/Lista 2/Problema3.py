l1 = float(input()) #Jean-Lucas Luquetti Silva / RA: 120443
l2 = float(input())
l3 = float(input())
if (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1): #condição de existência de um triângulo
	print('invalido')
elif (l1 == l2) and (l2 == l3): #Sequência de comparação entre os lados, para se determinar qual triângulo é
	print('equilatero')
elif (l1 == l2) or (l1 == l3) or (l2 == l3):
	print('isosceles')
else :
	print('escaleno')