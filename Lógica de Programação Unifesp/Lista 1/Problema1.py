n1 = int(input()) #Jean-Lucas Luquetti Silva / RA: 120443
n2 = int(input())
n3 = int(input())
menor = n1 #auxiliar que dirá qual dos valores comparados é o menor
if (n2 < menor): #sequência de condicionais que comparam os valores entre si, determinando o maior e o menor.
    menor = n2
if (n3 < menor):
    menor = n3
print(menor)