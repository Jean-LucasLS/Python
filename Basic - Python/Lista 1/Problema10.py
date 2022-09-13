idade = int(input()) #Jean-Lucas Luquetti Silva / RA: 120443
if idade > -1 and idade < 3: #sequência de condicionais para determinar a idade fornecidade e interpretar
	print('recém-nascido')
elif idade > 2 and idade < 12:
	print('criança')
elif idade > 11 and idade < 20:
	print('adolescente')
elif idade > 19 and idade < 66:
	print('adulto')
else :
	print('idoso')