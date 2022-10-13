n = int(input()) #Jean-Lucas Luquetti Silva / RA: 120443
pot = 1 #pot será o auxiliar do número que será elevado ao quadrado
valor = int() #esse será o valor da potência
while (n != 0): #um while criado para que o número N tenha todos os seus quadrados
    valor = pot*pot
    print(valor)
    pot = pot + 1
    n = n - 1