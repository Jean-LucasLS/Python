h = float(input()) #Jean-Lucas Luquetti Silva / RA: 120443
p = float(input())
sexo = input()
valor = float()
if (sexo == 'M'): #condicional que funciona baseado na letra dada
    valor = 72.7 * h - 58 #cálculo para M
    if (p > valor): #condicional que será ativada após a outra que determina o sexo dado, e com base no valor obtido dirá como está o peso
        print('acima')
    elif (p < valor):
        print('abaixo')
    else :
        print('peso ideal')
if (sexo == 'F'): #a outra condicional
    valor = 62.1 * h - 44.7 #cálculo para F
    if (p > valor): #mesmo sistema de condicional só que para o feminimo
        print('acima')
    elif (p < valor):
        print('abaixo')
    else :
        print('peso ideal')