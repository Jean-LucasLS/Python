n = int(input()) #Jean-Lucas Luquetti Silva / RA: 120443
div = 0 #Número de valores que podem dividir "n"
for count in range(2,n): #Operação que verifica o resto de divisão de 2 até o valor abaixo de "n"
    if (n % count == 0):
        div = div + 1
if(div == 0): #se nenhum número além de 1 e o próprio "n" conseguir dividi-lo, então ele será primo
    print('sim')
else :
    print('nao')