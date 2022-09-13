n1 = int(input()) #Jean-Lucas Luquetti Silva / RA: 120443
n2 = int(input())
n3 = int(input())
auxiliar = int
if (n3 > n2): #sequência de condicionais que manipularão os valores (através de um auxiliar) para trocá-los de acordo com a comparação entre maiores e menores
    auxiliar = n3
    n3 = n2
    n2 = auxiliar
if (n2 > n1):
    auxiliar = n2
    n2 = n1
    n1 = auxiliar
if (n3 > n2):
    auxiliar = n3
    n3 = n2
    n2 = auxiliar
print(n1)
print(n2)
print(n3)