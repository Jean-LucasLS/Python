n = int(input()) #Jean-Lucas Luquetti Silva / RA: 120443
aux = 0 #auxiliar que servirá para contar até N
soma = float(0)
while (n > aux): #laço que soma os números dados
    add = int(input())
    aux = aux + 1
    soma = soma + add
soma = soma / n #média aritmética
print('{:.4f}'.format(soma))