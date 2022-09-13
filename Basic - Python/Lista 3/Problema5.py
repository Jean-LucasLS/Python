numbers = [20, 45, 37, 22, 60] #Jean-Lucas Luquetti Silva / RA: 120443
maior = 20 #Declarando um número para ser comparado no laço
menor = 20 #Mesma coisa do maior
for num in numbers: #Laço de comparação para achar o maior
    if (num > maior):
        maior = num
for num in numbers: #Laço de comparação para achar o menor
    if (num < menor):
        menor = num
print(menor)
print(maior)