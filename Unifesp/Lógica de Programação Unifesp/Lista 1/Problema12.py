n = int(input()) #Jean-Lucas Luquetti Silva / RA: 120443
aux = 0 #auxiliar que servirá para contar até N
soma = 0
while (aux+1 < n): #laço que somará os números até N, de 2 em 2 no aux para só considerar os pares
 	aux = aux + 2
 	soma = soma + aux
print(soma)