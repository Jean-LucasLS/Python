numero = int(input())#Jean-Lucas Luquetti Silva / RA: 120443
lista = [] #declaração da lista
cont = 0 #contador para auxiliar no laço
for i in range(numero):
    lista.append(cont) #comando para adicionar os números na lista de um em um até o valor que foi dado
    cont += 1
print(lista)